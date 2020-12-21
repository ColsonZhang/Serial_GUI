from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from bokeh.server.server import Server
from bokeh.themes import Theme
from bokeh.models import ColumnDataSource, Slider, TextInput, Button ,Div , Text
from bokeh.layouts import column, row
from bokeh.models import CustomJS

from functools import partial
from threading import Thread
import threading
from tornado import gen
from random import random
import time

import serial
import serial.tools.list_ports

import myserial
import mythread


data = [0]
portx="COM1"
bps=9600
timex=5

flag_control = [False,False]

# flag_connect = True
# flag_disconnect = False
# flag_start = False
# flag_stop = False

def bkapp(doc):
    global flag_control

    def callback_button_open():
        flag_control[0] = True
        print("button successful")

        
    def callback_button_close():
        flag_control[1] = True
        print("button close suffess")
        pass
        # flag_connect = False
        # flag_disconnect = True
        
    def callback_button_start():
        print("button start pressed!!!!!!!!!!!!!!")
        pass    
    def callback_button_stop():
        print("button stop pressed")
        pass    

    source = ColumnDataSource(data=dict(x=[], y=[]))

    plot = figure(plot_height=400, plot_width=800,title="serial data wave",
              tools="crosshair,pan,reset,save,wheel_zoom",)

    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    text_port = TextInput(title="PORT", value='COM1')
    text_bps = TextInput(title="bps", value='9600')

    button_open = Button(label='Open', width=120, button_type = "success")
    button_open.on_click(callback_button_open)

    button_close = Button(label='Close', width=120, button_type = "success")
    button_close.on_click(callback_button_close)

    button_start = Button(label='Start', width=120, button_type = "success")
    # button_start.on_click(callback_button_start)
    button_start.js_on_click(CustomJS(code="alert('button: click!')"))

    button_stop = Button(label='Stop', width=120, button_type = "success")
    button_stop.on_click(callback_button_stop)
    
    control = column(text_port,text_bps,button_open,button_close,button_start,button_stop)

    @gen.coroutine
    def update(x, y):
        # source.stream(dict(x=[x], y=[y]))
        source.data =  dict(x=x, y=y)

    def blocking_task():
        global data
        while True:
            # do some blocking computation
            time.sleep(0.02)
            yin = data[:-1]
            xin = range(len(yin))
            # but update the document from callback
            doc.add_next_tick_callback(partial(update, x=xin, y=yin))
    
    
    layout_top = row(control,plot,name='top')
    doc.add_root(layout_top)
    thread = Thread(target=blocking_task)
    thread.start()


class myThread4 (threading.Thread):
    def __init__(self, portx, bps, timex, container, control):
        threading.Thread.__init__(self)
        self.Flag = True
        self.ser = SerialConnect(portx, bps, timex)
        self.container = container
        self.control = control
        print("thread4 is running !!!!!!!!")

    def run(self):
        flag_ctr_connect = False
        flag_ctr_disconnect = False
        
        while(True):
            if(not self.Flag):
                break
            else:
                if((not flag_ctr_connect) and self.control[0]):
                    print("\n\n Open the serial!!!!!!!!!!!!!\n\n")
                    flag_ctr_connect = True
                    flag_ctr_disconnect = False
                    self.ser.Open_Serial()

                # if((not flag_ctr_disconnect) and flag_disconnect):
                #     print("\n\n Close the serial~~~~~~~~~~~~n\n")
                #     flag_ctr_connect = False
                #     flag_ctr_disconnect = True
                #     self.ser.Close_Serial()    
                            
                if(flag_ctr_connect):
                    # print("doing")
                    data_term = self.ser.Read_Data()
                    if(len(data_term)>0):
                        data_process(data_term,self.container)
                else:
                    time.sleep(0.05)
            
                if(self.control[1]):
                    print("!!!!!!!!!!!!!!  break  !!!!!!!!!!!!")
                    break

def data_process(data_raw,data):
    data_raw = data_raw.decode('utf-8')
    data_temp = 0
    try:
        data_temp = int(data_raw.replace("s","").replace("e\n",""))
    except:
        print(data_raw)
    data.append(data_temp)


class myThread_ctr (threading.Thread):
    def __init__(self,theThread):
        threading.Thread.__init__(self)
        self.theThread = theThread

    def run(self):
        while(True):
            a = input()
            if a == "e":
                self.theThread.Flag = False
                break


class SerialConnect():
    def __init__(self, com, bps, timeout):
        self.port = com
        self.bps = bps
        self.timeout = timeout
    
    def Open_Serial(self):
        open_success = True
        try:
            self.serial = serial.Serial(self.port,self.bps,timeout=self.timeout, parity=serial.PARITY_NONE, stopbits=1)
            print("Open Sucess!")
        except Exception as e :
            open_success = False
            print("--ERROR--: ", e)
        return open_success

    def Close_Serial(self):
        self.serial.close()
        print("Close Successful ? ",bool(self.serial.is_open))

    def Flush_Input(self):
        self.serial.flushInput()
    
    def Read_Data(self):
        return self.serial.readline()

# Setting num_procs here means we can't touch the IOLoop before now, we must
# let Server handle that. If you need to explicitly handle IOLoops then you
# will need to use the lower level BaseServer class.
server = Server({'/': bkapp})
server.start()

if __name__ == '__main__':
    print('Opening Bokeh application on http://localhost:5006/')

    thread1 = myThread4(portx, bps, timex, data, flag_control)
    thread2 = myThread_ctr(thread1)
    thread1.start()
    thread2.start()

    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()

"""
==================================================================
name: app.py
purpose: the top module of the application
time: Dec 21. 2020
version: v1.0.0
author: Shen Zhang
==================================================================
"""


"""
=====================================================================
-------------------------IMPORT MODULE PART--------------------------
=====================================================================
"""
# import bokeh module
from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from bokeh.server.server import Server
from bokeh.themes import Theme
from bokeh.models import (AutocompleteInput,ColumnDataSource, Slider, TextInput, Button ,Div , Text, Select)
from bokeh.layouts import column, row
from bokeh.models import CustomJS
# import other module
from threading import Thread
from functools import partial
from tornado import gen
from random import random
import time
# import local module file
import myserial
import mythread

"""
=====================================================================
-------------------------INITIAL SETUP PART--------------------------
=====================================================================
"""
# data container
data = [0]
# serial info
serial_info = {"portx":"COM1",
               "bps":9600,
               "timex":0.5 }

# control container
flag_control_global = {"connect":False ,
                "disconnect":False,}


completions_bps = ["9600", "115200", "4800"]
completions_port = ["COM1", "COM2"]

"""
=====================================================================
-------------------------MAIN BOKEH APP PART-------------------------
=====================================================================
"""
def bkapp(doc):
    global flag_control_global
    global serial_info
    
    flag_control_local = {"start":False}

    def callback_button_open():
        serial_info["portx"] = select_port.value
        serial_info["bps"] = int(text_bps.value)
        flag_control_global["connect"] = True
        # flag_control_global["disconnect"] = False
        button_open.disabled = True
        button_close.disabled = False 
        print("button open successful")

    def callback_button_close():
        button_open.disabled=False
        button_close.disabled = True
        # flag_control_global["connect"] = False
        flag_control_global["disconnect"] = True
        print("button close successful")
        
    def callback_button_start():
        flag_control_local["start"] = True
        print("button start successful")
            
    def callback_button_stop():
        flag_control_local["start"] = False
        print("button stop successful")
            
    # def update_text_port(attrname, old, new):
    #     pass
    
    def update_select_port(attrnaem, old, new):
        pass

    def update_text_bps(attrname, old, new):
        pass

    source = ColumnDataSource(data=dict(x=[], y=[]))

    plot = figure(plot_height=400, plot_width=800,title="serial data wave",
              tools="crosshair,pan,reset,save,wheel_zoom",)

    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    # text_port = AutocompleteInput(title="PORT", value='COM1', completions=completions_port)
    # text_port.on_change('value', update_text_port)

    select_port = Select(title="PORT",value='COM1',options=["COM1", "COM2"])
    select_port.on_change('value', update_select_port)

    text_bps = AutocompleteInput(title="bps",value='9600',placeholder="Enter value (auto-complete) ...", completions=completions_bps)
    text_bps.on_change('value', update_text_bps)

    button_open = Button(label='Open', width=120, button_type = "success")
    button_open.on_click(callback_button_open)

    button_close = Button(label='Close', width=120, button_type = "success", disabled=True)
    button_close.on_click(callback_button_close)

    button_start = Button(label='Start', width=120, button_type = "success")
    button_start.on_click(callback_button_start)
    # button_start.js_on_click(CustomJS(code="alert('button: click!')"))

    button_stop = Button(label='Stop', width=120, button_type = "success")
    button_stop.on_click(callback_button_stop)
    
    control = column(select_port,text_bps,button_open,button_close,button_start,button_stop)

    @gen.coroutine
    def update(x, y, flag):
        global flag_control_global
        # source.stream(dict(x=[x], y=[y]))
        if(flag_control_local["start"]):
            source.data =  dict(x=x, y=y)
        
        if(flag_control_global["connect"]):
            button_open.disabled = True
            button_close.disabled = False 
        else:
            if(flag):
                select_port.options = refresh_com()

    def blocking_task():
        global data
        # global flag_control_global

        count = 0
        flag_update = False
        while True:
            # do some blocking computation
            time.sleep(0.02)
            flag_update = False
            count = count + 1
            if (count>=50):
                flag_update = True
                count = 0
            
            yin = data[:-1]
            xin = range(len(yin))
            # but update the document from callback
            doc.add_next_tick_callback(partial(update, x=xin, y=yin, flag=flag_update))
    
    layout_top = row(control,plot,name='top')
    doc.add_root(layout_top)
    thread_update_data = Thread(target=blocking_task)
    thread_update_data.start()



def refresh_com():
    available_port = ['COM1']
    com_available = myserial.SerialConnect.Get_Used_Com()
    if(len(com_available)>0):
        for com in com_available:
            available_port.append(com["device"])
    return available_port


# Setting num_procs here means we can't touch the IOLoop before now, we must
# let Server handle that. If you need to explicitly handle IOLoops then you
# will need to use the lower level BaseServer class.
server = Server({'/': bkapp})
server.start()


if __name__ == '__main__':

    print('Opening Bokeh application on http://localhost:5006/')

    thread1 = mythread.myThread4(serial_info, data, flag_control_global)
    thread2 = mythread.myThread_ctr(thread1)
    thread1.start()
    thread2.start()

    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()

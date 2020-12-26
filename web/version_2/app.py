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
# from bokeh.models import (AutocompleteInput,ColumnDataSource, Slider, TextInput, Button ,Div , Text, Select)
from bokeh.models import (AutocompleteInput, Button, CheckboxButtonGroup, CheckboxGroup,
                          ColorPicker, Column, ColumnDataSource, DataTable, DatePicker,
                          DateRangeSlider, DateSlider, Div, Dropdown, IntEditor,
                          MultiSelect, NumberEditor, NumberFormatter, Panel, Paragraph,
                          PreText, RadioButtonGroup, RadioGroup, RangeSlider, Row,
                          Select, SelectEditor, Slider, Spinner, StringEditor,
                          StringFormatter, TableColumn, Tabs, TextInput, Toggle,)
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
import DataContainer
"""
=====================================================================
-------------------------INITIAL SETUP PART--------------------------
=====================================================================
"""
# data container
# data = [0]
Data = DataContainer.DataContainer()
# Data.append(0)

# serial info
serial_info = {"portx":"COM1",
               "bps":9600,
               "timex":0.5 }

# control container
flag_control_global = {"connect":False ,
                       "disconnect":False,
                       "status":False}

"""
=====================================================================
-------------------------MAIN BOKEH APP PART-------------------------
=====================================================================
"""
def bkapp(doc):
    # global variables
    global flag_control_global
    global serial_info
    
    # local variables
    flag_control_local = {"start":False}
    
    # the period function
    @gen.coroutine
    def update(x, y, flag):
        global flag_control_global
        # source.stream(dict(x=[x], y=[y]))
        if(flag_control_local["start"]):
            if(len(y)>0):
                source.stream(dict(x=x, y=y))
            # source.data =  dict(x=x, y=y)    

        if(flag_control_global["status"]):
            button_open.disabled = True
            button_close.disabled = False 
        else:
            button_open.disabled = False
            button_close.disabled = True             
            if(flag):
                select_port.options = refresh_com()


    def blocking_task():
        global Data
        # global flag_control_global

        count = 0
        flag_update = False
        while True:
            # do some blocking computation
            time.sleep(0.05)
            flag_update = False
            count = count + 1
            if (count>=50):
                flag_update = True
                count = 0
            
            # yin = data[:-1]
            # xin = range(len(yin))
            yin,base_len = Data.get_buffer()
            xin = list(range(base_len-len(yin), base_len, 1))
            # but update the document from callback
            doc.add_next_tick_callback(partial(update, x=xin, y=yin, flag=flag_update))

    def refresh_com():
        available_port = []
        com_available = myserial.SerialConnect.Get_Used_Com()
        if(len(com_available)>0):
            for com in com_available:
                available_port.append(com["device"])
        return available_port

    # callback event of the button_open
    def callback_button_open():
        serial_info["portx"] = select_port.value
        serial_info["bps"] = int(text_bps.value)
        flag_control_global["connect"] = True
        # flag_control_global["disconnect"] = False
        button_open.disabled = True
        button_close.disabled = False 
        print("button open successful")

    # callback event of the button_close
    def callback_button_close():
        button_open.disabled=False
        button_close.disabled = True
        # flag_control_global["connect"] = False
        flag_control_global["disconnect"] = True
        print("button close successful")
    
    # callback event of the button_start
    def callback_button_start():
        button_start.disabled = True
        button_stop.disabled = False
        flag_control_local["start"] = True
        print("button start successful")
    
    # callback event of the button_stop
    def callback_button_stop():
        button_start.disabled = False
        button_stop.disabled = True
        flag_control_local["start"] = False
        print("button stop successful")
            
    # def update_text_port(attrname, old, new):
    #     pass
    
    def update_select_port(attrnaem, old, new):
        pass

    def update_text_bps(attrname, old, new):
        pass
    
    #------------------- data plot ---------------------------
    source = ColumnDataSource(data=dict(x=[], y=[]))
    plot = figure(plot_height=300, plot_width=1100,title="serial data wave",
              tools="crosshair,pan,reset,save,wheel_zoom",)
    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    # text_port = AutocompleteInput(title="PORT", value='COM1', completions=completions_port)
    # text_port.on_change('value', update_text_port)

    #------------------- port selector -----------------------
    select_port = Select(title="PORT",value='COM1',options=["COM1", "COM2"])
    select_port.on_change('value', update_select_port)

    #------------------- bps input ---------------------------
    completions_bps = ["9600", "115200", "4800"]
    text_bps = AutocompleteInput(title="bps",value='9600',placeholder="Enter value (auto-complete) ...", completions=completions_bps)
    text_bps.on_change('value', update_text_bps)

    #------------------- button on ---------------------------
    button_open = Button(label='Open', button_type = "success")
    button_open.on_click(callback_button_open)

    #------------------- button close ------------------------
    button_close = Button(label='Close', button_type = "success", disabled=True)
    button_close.on_click(callback_button_close)

    #------------------- button start ------------------------
    button_start = Button(label='Start', button_type = "success")
    button_start.on_click(callback_button_start)
    # button_start.js_on_click(CustomJS(code="alert('button: click!')"))

    #------------------- button stop ------------------------
    button_stop = Button(label='Stop', button_type = "success", disabled=True)
    button_stop.on_click(callback_button_stop)
    
    #------------------- widgets column ---------------------
    serial_control = column(select_port,text_bps,button_open,button_close,button_start,button_stop)

    #--------------------------------------------------------
    #------------------- set-parm layout --------------------
    #--------------------------------------------------------
    text_set_param_1 = TextInput(title="进样时间(s)", value='10')
    text_set_param_2 = TextInput(title="分离时间(s)", value='300')
    text_set_param_3 = TextInput(title="电极电位(伏)", value='214')
    text_set_param_4 = TextInput(title="采样频率(Hz)", value='20')
    text_set_param_5 = RadioGroup(labels=["循环伏安扫描", "电泳实验"], active=0)
    set_param = column(text_set_param_1,text_set_param_2,text_set_param_3,text_set_param_4,text_set_param_5)


    plot_slider_1 = Slider(title="基线位置",value=10, start=0, end=100, step=0.5)
    plot_slider_2 = Slider(title="幅度相调",value=20, start=0, end=100, step=0.5)
    plot_slider_3 = Slider(title="幅度粗调",value=60, start=0, end=100, step=0.5)
    plot_slider_4 = Slider(title="时间调节",value=40, start=0, end=100, step=0.5)
    plot_button_1 = Button(label="滤波", button_type="success")
    plot_slider = column(plot_slider_1,plot_slider_2,plot_slider_3,plot_slider_4,plot_button_1)

    ctr_button_0 = Button(label="使用说明", height=30, width=100, button_type="success")
    ctr_button_1 = Button(label="保存数据", height=30, width=100, button_type="success")
    ctr_button_2 = Button(label="清除数据", height=30, width=100, button_type="success")
    ctr_button_3 = Button(label="载入数据", height=30, width=100, button_type="success")
    ctr_button_4 = Button(label="加载参数", height=30, width=100, button_type="success")
    ctr_button_5 = Button(label="保存图像", height=30, width=100, button_type="success")
    ctr_button_6 = Button(label="指令交互", height=30, width=100, button_type="success")
    ctr_button_7 = Button(label="配置仪器", height=30, width=100, button_type="success")
    ctr_button = column(ctr_button_1,ctr_button_2,ctr_button_3,ctr_button_4,ctr_button_5,ctr_button_6,ctr_button_7)

    #--------------------------------------------------------
    #-------------------- Top layout ------------------------
    #--------------------------------------------------------
    layout_1 = row(plot)
    layout_2 = row(ctr_button,serial_control,set_param,plot_slider)
    # layout_3 = column(layout_1, layout_2)
    # layout_top = row(ctr_button,layout_3)
    layout_top = column(layout_1, layout_2)
    doc.add_root(layout_top)
    
    thread_update_data = Thread(target=blocking_task)
    thread_update_data.start()


# Setting num_procs here means we can't touch the IOLoop before now, we must
# let Server handle that. If you need to explicitly handle IOLoops then you
# will need to use the lower level BaseServer class.
server = Server({'/': bkapp})
server.start()


if __name__ == '__main__':

    print('Opening Bokeh application on http://localhost:5006/')

    thread1 = mythread.myThread4(serial_info, Data, flag_control_global)
    thread2 = mythread.myThread_ctr(thread1)
    thread1.start()
    thread2.start()

    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()

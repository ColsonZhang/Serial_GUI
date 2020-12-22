import PySimpleGUI as sg
from serial import Serial
from threading import Thread

 
com=('COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10')
baud_rate=('115200','9600','38400')
Stop_bit=('1','1.5','2')
data_bit=('8','7','6','5')
verify=('无','奇校验','偶校验')
 
 
layout1 =  [[sg.Text('COM口:'),sg.InputCombo(com,size=(15, 1))],
          [sg.Text('波特率:'),sg.InputCombo(baud_rate,size=(15, 1))],
          [sg.Text('停止位:'),sg.InputCombo(Stop_bit,size=(15, 1))],
          [sg.Text('数据位:'),sg.InputCombo(data_bit,size=(15, 1))],
          [sg.Text('奇偶位:'),sg.InputCombo(verify,size=(15, 1))],
          [sg.RButton('连接串口',size=(20,1))]]
 
button_size=(15,1)
 
Configure_button=[[sg.T('   '),sg.Text('响应测试',size=(15,1)),sg.T('   '),sg.Text('复位',size=(13,1)),sg.Text('设置模式',size=(15,1))],
        [sg.RButton('AT',size=button_size),sg.RButton('AT+RST',size=button_size),sg.RButton('AT+CWMODE=2',size=button_size)],
        [sg.T('   '),sg.Text('设置wifi名称 密码 通道 安全性'),sg.T(' '*15),sg.Text('开启多连接')],
        [sg.RButton('AT+CWSAP="esp8266","0123456789",11,3',size=(35,1)),sg.RButton('AT+CIPMUX=1')],
        [sg.T(' '),sg.Text('设置端口号')],
        [sg.RButton('AT+CIPSERVER=1,8080')]]
 
send_configure=[[sg.InputText('',key='input',size=(41,1)),sg.Checkbox('自动换行',default=True),sg.RButton('发送')]]
 
layout=[[sg.Multiline('',key='message',size=(29,5)),sg.Frame('',layout1)],
        [sg.Frame('命令配置',Configure_button)],
        [sg.Frame('发送区',send_configure)]
]
 
 
 
window=sg.Window('糖醋咸鱼ESP8266配置助手').Layout(layout)
 
ser=None
text=''
 
isRun=True
def readData():
    global isRun
    global text
    while isRun:
        if ser != None and ser.is_open:
            if text.count('\n')>5:
                text=text[text.index('\n')+1:]
            text+=ser.read().decode()
 
 
while True:
    button, value = window.ReadNonBlocking()
    window.FindElement('message').Update(text)
    if button==None and value==None:
        print('结束程序')
        isRun=False
        break
 
    if button=='连接串口':
        ser = Serial()
        ser.baudrate = int(value[1])  #波特率
        ser.port = value[0]    #com口
        ser.stopbits=int(value[2])     #停止位 1 1.5 2
        ser.bytesize=int(value[3])       #数据位
 
        if value[5]=='无':     #奇偶位  N没有  E偶数  O奇数
            ser.parity='N'
        elif value[5]=='奇校验':
            ser.parity = 'O'
        elif value[5] == '偶校验':
            ser.parity = 'E'
 
        ser.timeout=5       #超时时间
        try:
            ser.open()
            sg.Popup('连接成功')
            t = Thread(target=readData, name='read_data')
            t.start()   #开始线程
        except Exception as e:
            sg.Popup('连接失败')
 
    elif button=='发送':
 
        if ser!=None and ser.is_open:
            if value['input']!='':
                if value[5]==True:
                    ser.write((value['input']+'\n').encode())
                    ser.flush()
                else:
                    ser.write(value['input'].encode())
                    ser.flush()
                
            else:
                sg.Popup('请输入内容')
        else:
            sg.Popup('没有连接')
    else:
        window.FindElement('input').Update(button)    #修改发送框的内容
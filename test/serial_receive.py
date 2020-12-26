import serial
portx="COM7"
bps=9600
timex=1
text=''
#串口执行到这已经打开 再用open命令会报错
# ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1)

ser = serial.Serial()
ser.baudrate=bps
ser.port = portx
ser.dsrdtr = False
ser.setDTR(value=False)
ser.open()

# ser.dsrdtr = False
# ser.setDTR(level=False)
if (ser.isOpen()):
    print("open success")
     # 向端口些数据 字符串必须译码
    # ser.write("hello".encode())

    # while (True):
    #     if ser != None and ser.is_open:
    #         if text.count('\n')>5:
    #             text=text[text.index('\n')+1:]
    #         text+=ser.read().decode()
    while (True):
        # if ser.in_waiting:
        #     str=ser.read(ser.in_waiting ).decode("gbk")
        #     print(str)
        line = ser.readline()
        if(line):
            print(line)
            line=0
else:
	print("open failed")
ser.close()#关闭端口

import threading
import serial
import serial.tools.list_ports
import time
import array
import numpy as np

class SerialConnect():

    def __init__(self, com, bps, timeout):
        self.port = com
        self.bps = bps
        self.timeout = timeout

        try:
            self.serial = serial.Serial(self.port,self.bps,timeout=self.timeout, parity=serial.PARITY_NONE, stopbits=1)
        except Exception as e :
            print("--ERROR--: ", e)

    # 打印可用串口列表
    @staticmethod
    def Print_Used_Com():
        port_list = list(serial.tools.list_ports.comports())
        print(port_list)

    # 打印设备基本信息
    def Print_Name(self):
        print(self.serial.name) #设备名字
        print(self.serial.port)#读或者写端口
        print(self.serial.baudrate)#波特率
        print(self.serial.bytesize)#字节大小
        print(self.serial.parity)#校验位
        print(self.serial.stopbits)#停止位
        print(self.serial.timeout)#读超时设置
        print(self.serial.writeTimeout)#写超时
        print(self.serial.xonxoff)#软件流控
        print(self.serial.rtscts)#软件流控
        print(self.serial.dsrdtr)#硬件流控
        print(self.serial.interCharTimeout)#字符间隔超时
    
    # 打开串口
    def Open_Serial(self):
        self.serial.open()
    
    # 关闭串口
    def Close_Serial(self):
        self.serial.close()
        print("Close Successful ? ",bool(self.serial.is_open))
    
    def Flush_Input(self):
        self.serial.flushInput()

    def Write_Data(self,data):
        if(type(data)==str):
            self.serial.write(data.encode()) 
        else:
            self.serial.write((str(data)).encode()) 
    
    def Read_Data(self):
        return self.serial.readline()
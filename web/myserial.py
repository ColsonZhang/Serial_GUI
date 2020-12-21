"""
==================================================================
name: myserial.py
purpose: the class about the serial protocal
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
import serial
import serial.tools.list_ports
import numpy as np

"""
=====================================================================
---------------------------THE CLASS PART----------------------------
=====================================================================
"""
class SerialConnect():

    def __init__(self, ser_info):
        self.ser_info = ser_info
        # self.port = com
        # self.bps = bps
        # self.timeout = timeout


    @staticmethod
    def Get_Used_Com():
        used_com = []
        port_list = list(serial.tools.list_ports.comports())
        if( len(port_list) > 0 ):
            for p in port_list:
                used_com.append({"device":p.device, "name":p.name, "description":p.description })
        return used_com

    def Open_Serial(self):
        open_success = True
        try:
            self.serial = serial.Serial(self.ser_info["portx"],self.ser_info["bps"],timeout=self.ser_info["timex"], parity=serial.PARITY_NONE, stopbits=1)
            print("Open port ", self.ser_info["portx"], self.ser_info["bps"] ,"Sucess!")
        except Exception as e :
            open_success = False
            print("Open port ", self.ser_info["portx"], self.ser_info["bps"] ,"Failed!")
            print("--ERROR--: ", e)
        return open_success

    def Close_Serial(self):
        self.serial.close()
        print("Close Successful ? ",(not bool(self.serial.is_open)))

    def Flush_Input(self):
        self.serial.flushInput()
    
    def Read_Data(self):
        read_data = self.serial.readline()
        # to do:
        # deal with the timeout data
        try:
            read_data.decode('utf-8')
        except:
            print("error data:",read_data)
            read_data = "error"

        return read_data
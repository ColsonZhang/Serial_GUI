"""
==================================================================
name: myserial.py
purpose: the class about the serial protocal
time: Dec 21. 2020
version: v1.0.0
author: Shen Zhang
==================================================================
"""

import serial
import serial.tools.list_ports
import numpy as np


class SerialConnect():

    def __init__(self, ser_info):
        # Initial the Serial Class and cancel the DTR
        # Setting DTR's value False is important !!!
        # Or the device will always in the reset status
        self.serial = serial.Serial()
        self.serial.dsrdtr = False
        self.serial.setDTR(value=False)
        # copy the ser_info
        self.ser_info = ser_info

    # Get the avaliable port's information
    @staticmethod
    def Get_Used_Com():
        used_com = []
        port_list = list(serial.tools.list_ports.comports())
        if( len(port_list) > 0 ):
            for p in port_list:
                used_com.append({"device":p.device, "name":p.name, "description":p.description })
        return used_com

    # Set the serial's information
    def Set_Serial(self):
        self.serial.port = self.ser_info["portx"]
        self.serial.baudrate = self.ser_info["bps"]
        self.serial.timeout = timeout=self.ser_info["timex"]
        self.serial.parity = serial.PARITY_NONE
        self.serial.stopbits = 1

    # Open the selected serial port
    # Return whether the operation is successful
    def Open_Serial(self):
        open_success = True
        try:
            # self.serial = serial.Serial(self.ser_info["portx"],self.ser_info["bps"],timeout=self.ser_info["timex"], parity=serial.PARITY_NONE, stopbits=1)
            self.Set_Serial()
            self.serial.open()
            print("Open port ", self.ser_info["portx"], self.ser_info["bps"] ,"Sucess!")
        except Exception as e :
            open_success = False
            print("Open port ", self.ser_info["portx"], self.ser_info["bps"] ,"Failed!")
            print("--ERROR--: ", e)
        return open_success

    def Close_Serial(self):
        self.serial.close()
        close_success = not bool(self.serial.is_open)
        print("Close Successful ? ",close_success)
        return close_success

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
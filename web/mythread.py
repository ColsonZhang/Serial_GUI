"""
==================================================================
name: mythread.py
purpose: the class about the multi threads
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
import threading
import myserial
import time

"""
=====================================================================
---------------------------THE CLASS PART----------------------------
=====================================================================
"""

class myThread4 (threading.Thread):
    def __init__(self, ser_info, container, control):
        threading.Thread.__init__(self)
        self.Flag = True
        self.ser = myserial.SerialConnect(ser_info)
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
                if((not flag_ctr_connect) and self.control["connect"]):
                    print("-------------\nOpen the serial\n-------------")
                    self.control["connect"] = False
                    flag_ctr_connect = True
                    flag_ctr_disconnect = False
                    self.ser.Open_Serial()

                if((not flag_ctr_disconnect) and self.control["disconnect"]):
                    print("-------------\nClose the serial\n-------------")
                    self.control["disconnect"] = False
                    flag_ctr_connect = False
                    flag_ctr_disconnect = True
                    self.ser.Close_Serial()    
                            
                if(flag_ctr_connect):
                    data_term = self.ser.Read_Data()
                    if(len(data_term)>0):
                        data_process(data_term,self.container)
                else:
                    time.sleep(0.05)
            

def data_process(data_raw,data):
    # to do:
    # deal with the error data
    if(data_raw=="error"):
        pass
    else:
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

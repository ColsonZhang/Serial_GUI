import serial
import numpy as np
import time
import threading

portx="COM2"
bps=9600
timex=5
#串口执行到这已经打开 再用open命令会报错
exit = 0 

class myThread1 (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        index = 0
        while(True):
            if exit:
                break
            data_send = "s"+str(index)+"e\n"
            ser.write(data_send.encode())
            index = index + 1 
            if index > 200:
                index = 0
            time.sleep(0.05)

class myThread2 (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global exit ;
        a = input()
        if a == "e":
            exit = 1

ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1)
if (ser.isOpen()):
    print("open success")
else:
	print("open failed")


thread1 = myThread1()
thread2 = myThread2()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("exit!!!")

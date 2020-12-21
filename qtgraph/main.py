import threading
import time
import array
import numpy as np

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import sys

from myserial import *

class myThread1 (threading.Thread):
    def __init__(self,ser,container):
        threading.Thread.__init__(self)
        self.Flag = True
        self.ser = ser
        self.container = container

    def run(self):
        while(True):
            if(not self.Flag):
                break
            else:
                data_term = self.ser.Read_Data()
                if(len(data_term)>0):
                    data_process(data_term,self.container)


def data_process(data_raw,data):
    data_raw = data_raw.decode('utf-8')
    data_temp = 0
    try:
        data_temp = int(data_raw.replace("s","").replace("e\n",""))
    except:
        print(data_raw)
    data.append(data_temp)



class myThread2 (threading.Thread):
    def __init__(self,theThread):
        threading.Thread.__init__(self)
        self.theThread = theThread

    def run(self):
        while(True):
            a = input()
            if a == "e":
                self.theThread.Flag = False
                break


#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p6 = win.addPlot(title="Updating plot")
p6.enableAutoRange('xy', True)  ## stop auto-scaling after the first data set is plotted
curve = p6.plot(pen='y')

data = []

def update():
    # global curve, data, p6
    curve.setData(data)

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':

    portx="COM1"
    bps=9600
    timex=5
    ser = SerialConnect(portx, bps, timex)

    thread1 = myThread1(ser,data)
    thread2 = myThread2(thread1)

    thread1.start()
    thread2.start()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

    thread1.join()
    thread2.join()

    print("EXIT !!!")

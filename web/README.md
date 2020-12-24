# 开发日志

## 2020.12.22

* 当某个终端打开串口时，串口以及波特率的选择界面立马同步数据
* 修复 bug ：长时间读取数据时，串口close按键不好用，进程卡死，button组件无法调用callback函数
  * 这种情况通常发生在数据点大于2000个，有可能是data数据容器直接使用list列表造成的，需要对data-container优化
* 修复bug ：按下button-open或close时，两个button会频繁跳动一下

## 2020.12.24

* bug修复完成：调用pyerial 打开串口时，单片机直接卡死
  * bug 原因： 直接用下面语句打开串口时，会使能DTR，从而使得单片机一直处于不断复位的状态

    * `ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1)`
  * 修复方法：换用下面的打开方法

    * ```
      ser = serial.Serial()
      ser.baudrate=bps
      ser.port = portx
      ser.dsrdtr = False
      ser.setDTR(value=False)
      ser.open()
      ```

## to be continued

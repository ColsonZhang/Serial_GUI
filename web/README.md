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

# 2020.12.26

* 针对长时间读取数据时，Bokeh组件进程卡死，无法关闭串口的问题，进行了优化。
  * 将bokeh plot.line 的上传数据方法由全部数据上传，修改为流数据上传。

    ```
    source.stream(dict(x=x, y=y))
    # 替代以下方法
    # source.data =  dict(x=x, y=y)
    ```
  * 同时，优化是数据的存储结构。原来直接用list列表存储所有数据，现在用类对数据进行封装，在类的内部对数据存储进行优化，同时增加流数据上传的适配函数。
  * 对优化后的系统进行测试，发现在数据数目达到19000前，程序正常运行且无卡顿；数据数目22000时，程序仍能正常运行，但存在明显卡顿，CPU占用率过高。
* 将版本划分为version_1和version_2，version_2为优化后的版本。

## 2020.12.27

* 增加“退出系统”功能按键，解决调试时必须关闭终端，通过ctrl+c关闭无效的问题
* 在绘图栏，增加toolbars新功能；绘图模式方面，增加scatter 和line两种绘图模式

## 2020.12.28

* 进一步完善DataContainer类，新增保存csv和读取csv功能以及数据清除功能
* 进一步完善app功能，增加将串口数据导出到本地功能
* 进一步完善app功能，增加清除已经显示数据功能
* 进一步完善目标：
  * 保存数据时能够自定义路径和文件名
  * 增加从本地读取文件并进行显示的功能

## to be continued

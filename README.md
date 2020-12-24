# Serial_GUI

# 项目介绍

本项目包含两个子项目：1. web版本的上位机界面；2. 基于pyqt的本地上位机界面。

## web版本简介

本项目是基于bokeh开发的跨平台web上位机界面。

将下位机硬件通过串口与服务器（树莓派或其他能够支持Python运行的微机）连接，在服务器上运行该app。

用户终端与该服务器连接至同一个局域网后，可以直接访问http://localhost:5006/ ，即跳转到控制界面。

### 使用说明

一、安装python 3.x

二、安装必要的python功能包

在安装完成python后，对于window用户，可以按win+r键，输入cmd，调出命令行，输入以下命令安装功能包（如果安装完成后执行程序仍然报错，可以查看报错信息，是否有其他缺少安装的包）

```
pip install numpy
pip install bokeh
pip install pyserial
pip install tornado
pip install functools
```

三、执行程序

按win+r键，输入cmd，调出命令行，在命令行中进入项目目录（Serilal_GUI文件夹下）；或者打开Serilal_GUI文件夹，点击文件资源管理器中的文件路径一栏，清空路径，输入cmd，在当前路径下调出目录。

执行以下命令

`cd web`

`python app.py`

键入命令并执行后，会自动弹出web窗口，也可以通过浏览器输入http://localhost:5006/  打开

## qt版本简介

本项目是基于pyqt5和pyqtgraph开发的跨平台python-gui应用。

将下位机硬件通过串口与服务器（树莓派或其他能够支持Python运行的微机）连接，在服务器上运行该app。

用户可以在该服务器本地上运行该程序。

# 项目目录

* qtgraph
  * qt版本的GUI程序
* web
  * web版本GUI程序
* test
  * 用于本地调试的程序

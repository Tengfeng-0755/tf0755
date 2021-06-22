#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__ = "Teng Feng"
# __date__ = "2021/06/15"
# __Desc__ = 提供对多个不同web站点的一键登录功能，并允许用户自行录入用户名及密码
#应用集成经常遇到各个子系统需要web登录的情况，比如海康的NVR，
#做了一个应用，允许用户把自己的几个子系统的用户名+密码+url录入，然后一键登录所有录入了信息的子系统。

#用了个新的GUI框架，贴例程在下面
# import PySimpleGUI as sg
#
# sg.ChangeLookAndFeel('GreenTan')
#
# form = sg.FlexForm('Everything bagel', default_element_size=(40, 1))
#
# column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10,1))],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
# layout = [
#     [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
#     [sg.Text('Here is some text.... and a place to enter text')],
#     [sg.InputText('This is my text')],
#     [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
#     [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
#     [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
#      sg.Multiline(default_text='A second multi-line', size=(35, 3))],
#     [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
#      sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
#     [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
#      sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
#      sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
#      sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
#      sg.Column(column1, background_color='#d3dfda')],
#     [sg.Text('_'  * 80)],
#     [sg.Text('Choose A Folder', size=(35, 1))],
#     [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
#      sg.InputText('Default Folder'), sg.FolderBrowse()],
#     [sg.Submit(), sg.Cancel()]
#      ]
#
# button, values = form.LayoutAndRead(layout)
# sg.MsgBox(button, values)
#常用控件说明
# Text：文本
# InputText：输入框
# InputCombo：下拉列表框
# Multiline:大文本框
# Listbox：多行列表文本框
# Checkbox：多选框
# Radio：单选框
# Slider：拖动按钮
# FolderBrowse：选取文件夹
# FilerBrowse：选取文件
# Button：按钮
# Quit：
# Cancel：取消
# Menu：菜单
# Column：列
# Frame：块

import time
import PySimpleGUI as sg
import os

#使用PySimpleGUI做界面，用os进行文件操作
# open 函数
# file object = open(file_name [, access_mode][, buffering])
# 各个参数的细节如下：
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
#config_gui()
def config_gui():
#打开login_config文件，没有就创建并打开
    fo = open("login_config.txt","a+")
    login_systerm_name = []
    login_url_list = []
    str = fo.read()
    print("读取的内容：",str)

#配置界面
    sg.ChangeLookAndFeel('GreenTan')
#主界面
    layout = [[sg.Text('已录入系统：')],
              [sg.Text(login_systerm_name)]
              [sg.Text('请填写登录系统名称，url，账号，密码')],
              [sg.Text('系统名称：'),sg.InputText()],
              [sg.Text('系统url：'),sg.InputText()],
              [sg.Text('账号：'),sg.InputText()],
              [sg.Text('密码：'),sg.InputText()],
        [sg.Button('保存'),sg.Button('下一个'),sg.Button('取消')]
    ]
    config_window = sg.Window('配置功能主界面',layout)

    while True:
        event, values = config_window.read()
        if event in ('保存', '下一个', '取消'):
            break


def login_gui():
    sg.ChangeLookAndFeel('GreenTan')
    main_button_choices = ("一键登录","站点配置","退出系统")
    login_url_list = []
#主界面
    layout = [[sg.Text('仅供学习使用，如造成损失，使用者责任自负！')],
        [sg.Button('一键登录'),sg.Button('站点配置'),sg.Button('退出系统')]
    ]
    main_window = sg.Window('一键登录功能主界面',layout)
    while True:
        event,values = main_window.read()
        if  event in ('一键登录','站点配置','退出系统'):
            break
    main_window.close()
    if event == main_button_choices[0]:
#显示config_txt里的url和选择框
        layout = [[sg.Text('一键登录的系统可以多选')],
                  [sg.Checkbox(main_button_choices[0],default=True),sg.Checkbox(main_button_choices[1]),sg.Checkbox(main_button_choices[1])],#多选框；
                  [sg.Radio(main_button_choices[0],"RADIO1",default=True),sg.Radio(main_button_choices[1],"RADIO1"),sg.Radio(main_button_choices[1],"RADIO1")],#单选框；
                  [sg.Button('一键登录站点'), sg.Button('web设置'), sg.Button('终止程序')]
                  ]
        login_url_window = sg.Window('选择一键登录网站的界面', layout)
        while True:
            event,values = login_url_window.read()
            if  event in ('一键登录站点','web设置','终止程序'):
                break


        login_url_window.close()
    elif event == main_button_choices[1]:
        config_gui()
    elif event == main_button_choices[2]:
        exit()
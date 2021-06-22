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
import time
import PySimpleGUI as sg
import os

#使用PySimpleGUI做界面，用os进行文件操作

#config_gui()
def config_gui():
#打开login_config文件，没有就创建并打开
    fo = open("login_config.txt",os.O_RDWR|os.O_CREAT)

def login_gui():
    main_button_choices = ("一键登录","web设置","终止程序")
    choices_fieldnames = [];
#主界面
    button_return = g.buttonbox('仅供学习使用，如造成损失，使用者责任自负！','一键登录站点',choices=("一键登录","web设置","终止程序"))
    if button_return == main_button_choices[0]:
#取出已经录入的
        choice_return = g.multchoicebox('请选择要登录的站点，可多选','',choices=choices_fieldnames)
    elif button_return == main_button_choices[1]:
        config_gui()
    elif button_return == main_button_choices[2]:
        exit()
#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__ = "Teng Feng"
# __date__ = "2021/02/02"
# __Desc__ = 封装GUI
#对于大部分的EasyGui函数都有默认参数，几乎所有的组件都会显示一个消息和标题。
#标题默认是空字符串，信息通畅有一个简单的默认值
#各API简介
#msgbox()函数
#msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None)
#msgbox() 显示一个消息和提供一个"OK"按钮，你可以指定任意的消息和标题，你甚至可以重写"OK"按钮的内容


#ccbox()函数
#ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None)
#ccbox() 提供一个选择：Continue 或者 Cancel，并相应的返回 1（选中Continue）或者 0（选中Cancel）。注意 ccbox() 是返回整型的 1 或 0，不是布尔类型的 True 或 False。
#msg = g.msgbox("Hello Easy GUI")
#当然你也可以指定信息参数和标题参数
#title = g.msgbox(msg="我一定要学会编程！",title="标题部分",ok_button="加油")

#ynbox()函数，和ccbox()函数一样

#buttombox()
#buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
#可以使用 buttonbox() 定义自己的一组按钮，buttonbox() 会显示一组你定义好的按钮。
#当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。如果用户取消取消或者关闭窗口，那么会返回默认选项（第一个选项）。
#g.buttonbox(msg="你喜欢下面哪种水果?",title="",choices=("西瓜","苹果","草莓"))
#当你调用一个 buttonbox 函数（例如 msgbox(), ynbox(), indexbox() 等等）的时候，
#你还可以为关键字参数 image 赋值，这是设置一个 .gif 格式的图像（注意仅支持 GIF 格式哦）
#g.buttonbox("大家说嗅嗅可爱吗?",image="xiuxiu.gif",choices=("可爱","不可爱","财迷"))

#indexbox()
#indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)
#基本跟上面一样，区别就是当用户选择第一个按钮的时候返回序列号0，选择第二个按钮时候返回序列号1。

#boolbox()
#boolbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)
#如果第一个按钮被选中则返回 1，否则返回 0。

#choicebox()
#按钮组件方便提供用户一个简单的按钮选项，但如果有很多选项，或者选项的内容特别长的话，更好的策略是为它们提供一个可选择的列表。
#choicebox() 为用户提供了一个可选择的列表，使用序列（元祖或列表）作为选项，这些选项显示前会按照不区分大小写的方法排好序。
#另外还可以使用键盘来选择其中一个选项（比较纠结，但一点儿都不重要）：
#例如当按下键盘上的"g"键，将会选中的第一个以"g"开头的选项。
#再次按下"g"键，则会选中下一个以"g"开头的选项。
#在选中最后一个以"g"开头的选项的时候，再次按下"g"键将重新回到在列表的开头的第一个以"g"开头的选项。
#如果选项中没有以"g"开头的，则会选中字符排序在"g"之前（"f"）的那个字符开头的选项。
#如果选项中没有字符的排序在"g"之前的，那么在列表中第一个元素将会被选中。
#综合我们之前学习的文件功能，举个通俗的例子
#msg = "选择你喜欢的一种业余生活"
#title = ""
#choicess_list = ["看书","游泳","骑自行车","玩游戏"]
#reply = g.choicebox(msg,choices=choicess_list)

#multchoicebox()
#multchoicebox(msg='Pick as many items as you like.', title=' ', choices=(), **kwargs)
#multchoicebox() 函数也是提供一个可选择的列表，与 choicebox() 不同的是，multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。
#multchoicebox() 函数也是使用序列（元祖或列表）作为选项，这些选项显示前会按照不区分大小写的方法排好序。
#g.multchoicebox(msg="请选择你爱吃哪些水果?",title="",choices=("西瓜","香蕉","苹果","梨"))
#g.multchoicebox(msg="请选择你爱吃哪些水果?",title="",choices=("西瓜","香蕉","苹果","梨"))

#enterbox()
#enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
#enterbox() 为用户提供一个最简单的输入框，返回值为用户输入的字符串。
#默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。
#g.enterbox(msg="请说出此时你的心里话",title="心里悄悄话")

#integerbox()
#integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)
#integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入。
#g.integerbox(msg="请输入您的得分",title="分数计",lowerbound=0,upperbound=100)

#multenterbox()
#multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
#multenterbox() 为用户提供多个简单的输入框，要注意以下几点：
#如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
#如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
#如果用户取消操作，则返回域中的列表的值或者None值
# msg = "请填写一下信息(其中带*号的项为必填项)"
# title = "账号中心"
# fieldNames = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","*Email"]
# fieldValues = []
# fieldValues = g.multenterbox(msg,title,fieldNames)
# #print(fieldValues)
# while True:
#     if fieldValues == None :
#         break
#     errmsg = ""
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#             errmsg += ("【%s】为必填项   " %fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
# print("您填写的资料如下:%s" %str(fieldValues))

# passwordbox()
# passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)
# passwordbox() 跟 enterbox() 样式一样，不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串：
# g.passwordbox(msg="请输入您的密码")
# user_password = g.passwordbox(msg)
# print(str(user_password))

# multpasswordbox()
# multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
# multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（"*"）：
# msg = "请输入用户名和密码"
# title = "用户登录接口"
# user_info = []
# user_info = g.multpasswordbox(msg,title,("用户名","密码"))
# print(user_info)

# textbox()
# textbox(msg='', title=' ', text='', codebox=0)
# textbox() 函数默认会以比例字体（参数 codebox=1 设置为等宽字体）来显示文本内容（会自动换行哦），这个函数适合用于显示一般的书面文字。
# 注：text 参数（第三个参数）可以是字符串类型，列表类型，或者元祖类型。

# diropenbox()
# diropenbox(msg='',title='',default='')
# 该函数用于提供一个对话框，返回用户选择的目录名，该目录名是带有完整的路径的
# 选择Cancel的话，返回值默认为None
# msg = '选择一个文件，将会返回该文件的完整的目录'
# title = '文件选择对话框'
# default = r'F:flappy-bird'
# full_file_path = easygui.diropenbox(msg,title,default)
# print('选择的文件的完整的路径为：'+str(full_file_path))

# fileopenbox()
# fileopenbox(msg=None, title=None, default='*', filetypes=None)
# fileopenbox()
# 函数用于提供一个对话框，返回用户选择的文件名（带完整路径哦），如果用户选择
# "Cancel"则返回None。
# 关于default参数的设置方法：
# default参数指定一个默认路径，通常包含一个或多个通配符。
# 如果设置了default参数，fileopenbox()显示默认的文件路径和格式。
# default默认的参数是'*'，即匹配所有格式的文件。
#
# default = "c:/fishc/*.py"即显示C:\fishc文件夹下所有的Python文件。
# default = "c:/fishc/test*.py"即显示C:\fishc文件夹下所有的名字以test开头的Python文件。
#
# 关于filetypes参数的设置方法：
# 可以是包含文件掩码的字符串列表，例如：filetypes = ["*.txt"]
# 可以是字符串列表，列表的最后一项字符串是文件类型的描述，例如：filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]]

# filesavebox()
# filesavebox(msg=None, title=None, default='', filetypes=None)
# filesavebox() 函数提供一个对话框，让用于选择文件需要保存的路径（带完整路径哦），如果用户选择"Cancel"则返回 None。
# default 参数应该包含一个文件名（例如当前需要保存的文件名），当然你也可以设置为空的，或者包含一个文件格式掩码的通配符。
# filetypes 参数的设置方法请参考上边

# EgStore类
# GUI 编程中一个常见的场景就是要求用户设置一下参数，然后保存下来，以便下次用户使用你的程序的时候可以记住他的设置。
# 为了实现对用户的设置进行存储和恢复这一过程，EasyGui 提供了一个叫做 EgStore 的类。为了记住某些设置，你的应用程序必须定义一个类（暂时称之为"设置"类，尽管你随意地使用你想要的名称设置它）继承自 EgStore 类。
# 然后你的应用程序必须创建一个该类的对象（暂时称之为"设置"对象）。
# 设置类的构造函数（__init__ 方法）必须初始化所有的你想要它所记住的那些值。
# 一旦你这样做了，你就可以在"设置"对象中通过设定值去实例化变量，从而很简单地记住设置。之后使用 settings.store() 方法在硬盘上持久化设置对象。
# 除了例子里面的# user，server，可以添加任何你想添加的项目，比如IP，PORT，等等
# 下面是创建一个"设置"类的例子：
# # -----------------------------------------------------------------------
# # create "settings", a persistent Settings object
# # Note that the "filename" argument is required.
# # The directory for the persistent file must already exist.
# # -----------------------------------------------------------------------
# settingsFilename = os.path.join("C:", "FishCApp", "settings.txt")  # Windows example
# settings = Settings(settingsFilename)
#
# 下面是使用"设置"对象的例子：
#
# # we initialize the "user" and "server" variables
# # In a real application, we'd probably have the user enter them via enterbox
# user = "奥巴马"
# server = "白宫"
#
# # we save the variables as attributes of the "settings" object
# settings.userId = user
# settings.targetServer = server
# settings.store()  # persist the settings
#
# # run code that gets a new value for userId
# # then persist the settings with the new value
# user = "小甲鱼"
# settings.userId = user
# settings.store()

# exceptionbox()捕获异常
# 使用 EasyGui 编写 GUI 程序，有时候难免会产生异常。当然这取决于你如何运行你的应用程序，当你的应用程序崩溃的时候，堆栈追踪可能会被抛出，或者被写入到 stdout 标准输出函数中。
# EasyGui 通过 exceptionbox() 函数提供了更好的方式去处理异常，异常出现的时候，exceptionbox() 会显示堆栈追踪在一个 codebox() 中并且允许你做进一步的处理。
# exceptionbox() 很容易使用，下面是一个例子：
# try:
#         print('I Love FishC.com!')
#         int('FISHC') # 这里会产生异常
# except:
#         exceptionbox()
# -*- coding:utf-8 -*-
# import os
# import pickle
import time
import easygui as g
from easygui import EgStore
from tf0755_git.WebApp.mouse_webapp import mouse_event,mouse_click_botton   #重装系统后，重新安装3.8，语法又要求带相对路径
# from WebApp.mouse_webapp  import  mouse_event,mouse_click_botton
# from WebApp.mouse_webapp  import   mouse_press_test,mouse_listen_test   #调用同一项目下不同目录文件的函数
class Settings(EgStore):
    def __init__(self, filename):  # filename is required
        # -------------------------------------------------
        # Specify default/initial values for variables that
        # this particular application wants to remember.
        # -------------------------------------------------
        self.userId = ""
        self.usr_structor = ""
        self.App_IP_config = ""
        self.App_Port_config = ""

        # -------------------------------------------------
        # For subclasses of EgStore, these must be
        # the last two statements in  __init__
        # -------------------------------------------------
        self.filename = filename  # this is required
        # self.restore()
def config_gui():
# 配置页面
# config1 = g.read_or_create_settings("./settings.txt")   #貌似没起作用，创建文件的是下面的代码

    settingFile = "settings.txt"
    config_app = Settings(settingFile)
    usr_id = "tjx"
    usr_structor = "peidao"
    APP_IP_config = "192.168.19.1"
    config_app.userId = usr_id
    config_app.usr_structor = usr_structor
    config_app.App_IP_config = APP_IP_config
    config_app.store()
    print("\nInitial settings")
    print(config_app)

    time.sleep(20)
#修改配置内容GUI
    msg = "请填写要修改的配置"
    title = "参数配置"
    fieldNames = ["*用户名","*机构名","IP","Port"]
    fieldValues = []
    fieldValues = g.multenterbox(msg,title,fieldNames)
    while True:
        if fieldValues == None :
            break
        errmsg = ""
        for i in range(len(fieldNames)):
            option = fieldNames[i].strip()
            if fieldValues[i].strip() == "" and option[0] == "*":
                errmsg += ("【%s】为必填项   " %fieldNames[i])
        if errmsg == "":
            break
        fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
    print("您填写的资料如下:%s" %str(fieldValues))

#修改配置文件
    usr_id = fieldValues[0]
    usr_structor = fieldValues[1]
    APP_IP_config = fieldValues[2]
    APP_Port_config = fieldValues[3]
    config_app.userId = usr_id
    config_app.usr_structor = usr_structor
    if(APP_IP_config != ''):            #空字符串的表示方法，和空值（None）是不一样的。
        config_app.App_IP_config = APP_IP_config
    if(APP_Port_config != ''):
        config_app.App_Port_config = APP_Port_config
    config_app.store()
    print("\nInitial settings")
    print(config_app)

def xunmo_run():
    mouse_obj = mouse_event

    count = 0
    while   count < 10:
        # 到达指定位置，按下左键
        print('墨侠')
        # move是移动到当前的相对位置，所以要先设定当前位置，再move，move的参数是相对误差（5，-5）,直接调用鼠标移动函数
        mouse_obj.point_set_x = 1268
        mouse_obj.point_set_y = 678
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到墨侠按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)

        print('寻墨')
        mouse_obj.point_set_x = 793
        mouse_obj.point_set_y = 384
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到寻墨按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)


        print('开始共鸣')
        mouse_obj.point_set_x = 1241
        mouse_obj.point_set_y = 365
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到开始共鸣按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)

        print('开始寻墨')
        mouse_obj.point_set_x = 1086
        mouse_obj.point_set_y = 585
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到开始寻墨按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)

        print('开始寻墨确认')
        mouse_obj.point_set_x = 964
        mouse_obj.point_set_y = 377
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到开始寻墨确认按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)

        print('自动探索')
        mouse_obj.point_set_x = 1036
        mouse_obj.point_set_y = 572
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到自动探索按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(5)

        print('自动探索确认')
        mouse_obj.point_set_x = 928
        mouse_obj.point_set_y = 346
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到开始寻墨确认按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(240)  #等待寻墨完成

        print('离开')
        mouse_obj.point_set_x = 1064
        mouse_obj.point_set_y = 557
        mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
        mouse_obj.mouse_point_move(mouse_obj)    # 移动到离开按钮
        mouse_obj.mouse_click(mouse_obj)  #按下左键
        time.sleep(2)  #等待寻墨完成

def app_gui():
    main_button_choices = ("日常任务","自动寻墨","自动爬塔","配置页面","终止程序")
    richang_button_choices = ("自动副本","自动阵图","自动璇玑","自动分解")
#主界面
    button_return = g.buttonbox('仅供学习使用，如造成损失，使用者责任自负！','蜀山传奇辅助脚本',choices=("日常任务","自动寻墨","自动爬塔","配置页面","终止程序"))
    if button_return == main_button_choices[0]:
        choice_return = g.multchoicebox('请选择自动打怪的类型，可多选','',choices=("自动副本","自动阵图","自动璇玑","自动分解"))
    elif button_return == main_button_choices[1]:
        xunmo_run()
    elif button_return == main_button_choices[3]:
        config_gui()


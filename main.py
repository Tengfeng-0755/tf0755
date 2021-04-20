# 这是一个专门为蜀山传奇页游做的一个自动化脚本。
# import win32gui
# import win32api
# import win32con
# from win32gui import *
import time
import PIL  #PIL不支持PY3,所以安装了pillow，原来PY2的代码用的PIL库也能引用了。
# import pynput   #其他诸如pymouse,pykeyboard，安装了都不能兼容，在3.8
# import easygui


import os,sys

from WebApp.mouse_webapp  import   mouse_press_test,mouse_listen_test   #调用同一项目下不同目录文件的函数
from WebApp.keyboard_webapp import      keyboard_listener,keyboard_press_test   #如果引用出问题，改为from tf0755_git.WebApp.keyboard_webapp import  keyboard_listener,keyboard_press_test,下同。
from WebApp.screenshot import screen_shot,screen_shot_fullscreen,screen_shot_box
from WebApp.compareimage_with_screen import match_image_test
from WebApp.sscq_run import game_run_test
from WebApp.Webapp_gui import app_gui
#   脚本是顺序运行



if __name__ == '__main__':
#自动点击指定位置
    # game_run_test()
    time.sleep(1)
#绘制一个界面，修改默认的config
    app_gui()
# 截屏
#     screen_shot_fullscreen()
#     box_l = [1,1,1500,1500]
#     screen_shot_box(box_l)
# 鼠标侦听
#     mouse_listen_test()
# 鼠标移动及点击
#     mouse_press_test()
# 模板匹配
#     match_image_test()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

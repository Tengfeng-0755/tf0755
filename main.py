# 这是一个专门为蜀山传奇页游做的一个自动化脚本。
import win32gui
import win32api
import win32con
from win32gui import *
import time
import PIL
import pynput   #其他诸如pymouse,pykeyboard，安装了都不能兼容，在3.8



import os,sys

from WebApp.mouse_webapp  import   mouse_press_test,mouse_listen_test   #调用同一项目下不同目录文件的函数
from WebApp.keyboard_webapp import      keyboard_listener,keyboard_press_test
from WebApp.screenshot import screen_shot,screen_shot_fullscreen,screen_shot_box
from WebApp.compareimage_with_screen import match_image_test
from WebApp.sscq_run import game_run_test
#   脚本是顺序运行



if __name__ == '__main__':
#自动点击指定位置
    # game_run_test()
    time.sleep(1)
#截屏
    # screen_shot_fullscreen()
    # box_l = [1,1,1500,1500]
    # screen_shot_box(box_l)
#鼠标侦听
    # mouse_listen_test()
#鼠标移动及点击
    # mouse_press_test()
#模板匹配
    # match_image_test()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

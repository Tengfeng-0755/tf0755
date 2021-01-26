# 这是一个专门为蜀山传奇页游做的一个自动化脚本。
import win32gui
import win32api
import win32con
from win32gui import *
import time
import PIL
import pynput   #其他诸如pymouse,pykeyboard，安装了都不能兼容，在3.8

from PIL import Image
from PIL import ImageGrab
import imagehash3

import os,sys

from WebApp.mouse_webapp  import   mouse_point_test,mouse_listener,mouse_press_test,mouse_scroll_test   #调用同一项目下不同目录文件的函数
from WebApp.keyboard_webapp import      keyboard_listener,keyboard_press_test
#   脚本是顺序运行

# 程序信息函数
def print_program_inf(name,ver):
    print(f'Programer name: {name}')  # 打印脚本名。
    print(f'Version: {ver}')  # 打印版本。

if __name__ == '__main__':
#    mouse_press_test()
#    pynput.mouse.Events()
#    pynput.mouse.Listener()
    x = "sscq自动脚本";y = "V1.00"
    print_program_inf(x,y)
    time.sleep(5)
    # mouse_point_test()
    # mouse_listener()
    # mouse_press_test()
    # mouse_scroll_test()
    # keyboard_listener()
    # keyboard_press_test()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

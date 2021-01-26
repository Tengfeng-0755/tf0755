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
from pynput import keyboard

#   脚本是顺序运行
#####################################################################
#鼠标函数族
def on_move(x,y):
    print('Pointer moved to {0}'.format((x,y)))

def on_click(x,y,button,pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x,y)))

def on_scroll(x,y,dx,dy):
    print('Scrolled {0} at  {1}'.format('down' if dy < 0 else 'up',(x,y)))

# 鼠标侦听函数
# Collect events until released
def mouse_listener():
    with    pynput.mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()


    # with pynput.mouse.Events() as event:
    #     for i in event:
    #         # 迭代用法。
    #         if isinstance(i, pynput.mouse.Events.Move):
    #             # 鼠标移动事件。
    #             print(i.x, i.y)
    #             # 不要直接打印`i`，模块这里有问题，会报错。
    #
    #         elif isinstance(i, pynput.mouse.Events.Click):
    #             # 鼠标点击事件。
    #             print(i.x, i.y, i.button, i.pressed)
    #             # 这个i.button就是上文所说的“鼠标按键”中的一个，用is语句判断即可。
    #
    #         elif isinstance(i, pynput.mouse.Events.Scroll):
    #             # 鼠标滚轮。
    #             print(i.x, i.y, i.dx, i.dy)
    #
    #         break
    #
    #     i = event.get(1)
    # 另一种用法。
    # 默认值是None。
    # 这个`1`就是最长等待时间，超过这个时间没有事件，
    # 就会报错。错误类型是queue模块的Empty，而非TimeoutError。

#  鼠标控制函数
def mouse_press_test():
    ctr = pynput.mouse.Controller()
    count = 0
    while   count < 10:
        # 到达指定位置，按下左键
        print('墨侠')
        # move是移动到当前的相对位置，所以要先设定当前位置，再move，move的参数是相对误差（5，-5）
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (1268, 678)  # 移动到墨侠按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(5)

        print('寻墨')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (793, 384)# 移动到寻墨按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(5)


        print('开始共鸣')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (1241, 365)  # 移动到开始共鸣按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(5)

        print('开始寻墨')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (1086, 585)  # 移动到开始寻墨按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(5)

        print('开始寻墨确认')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (964, 377)  # 移动到开始寻墨确认按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(5)

        print('自动探索')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (1036, 572)  # 移动到自动探索按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。

        time.sleep(5)

        print('自动探索确认')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (928, 346)  # 移动到开始寻墨确认按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(240)  #等待寻墨完成

        print('离开')
        print('The current pointer position is {0}'.format(
            ctr.position))
        # Set pointer position
        ctr.position = (1064, 557)  # 移动到离开按钮
        print('Now we have moved it to {0}'.format(
            ctr.position))
        # Move pointer relative to current position
        ctr.move(5, -5)
        ctr.press(pynput.mouse.Button.left)
        ctr.release(pynput.mouse.Button.left)   #释放左键。
        time.sleep(2)  #等待寻墨完成

def mouse_point_test():
    ctr = pynput.mouse.Controller()
    # Read pointer position
    print('The current pointer position is {0}'.format(
        ctr.position))

    # Set pointer position
    ctr.position = (1268, 678)
    print('Now we have moved it to {0}'.format(
        ctr.position))

    # Move pointer relative to current position
    ctr.move(5, -5)

#模拟滚轮上下滑动
def mouse_scroll_test():
    ctr = pynput.mouse.Controller()
    ctr.scroll(0, 500)
    # 向上滚动50单位。

    ctr.scroll(0, -500)
    # 向下滚动50单位。
#############################################

############################################
#键盘函数族
def on_press(key):
    '按下按键时执行。'
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    #通过属性判断按键类型。

def on_release(key):
    '松开按键时执行。'
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
#键盘侦听
def keyboard_listener():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

#键盘控制
def keyboard_press_test():
    ctr = pynput.keyboard.Controller()

    # with ctr.pressed(
    #         pynput.keyboard.Key.ctrl,
    #         pynput.keyboard.Key.shift,
    #         's'):
    #     pass
    # with ctr.pressed('s'):
    #     pass
#模拟按键 A
    # ctr.press('A')
    # ctr.release('A')
#模拟特殊按键ctrl+a，效果是当前页面全选
    with ctr.pressed(pynput.keyboard.Key.ctrl):
        ctr.press('a')
        ctr.release('a')

    time.sleep(0.3)

    with ctr.pressed(pynput.keyboard.Key.esc):
        pass
############################################

# 程序信息函数
def print_program_inf(name,ver):
    print(f'Programer name: {name}')  # 打印脚本名。
    print(f'Version: {ver}')  # 打印版本。

if __name__ == '__main__':
#    mouse_press_test()
#    pynput.mouse.Events()
#    pynput.mouse.Listener()
    x = "蜀山传奇自动脚本";y = "V1.00"
    print_program_inf(x,y)
    time.sleep(5)
    # mouse_point_test()
    # mouse_listener()
    mouse_press_test()
    # mouse_scroll_test()
    # keyboard_listener()
    # keyboard_press_test()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

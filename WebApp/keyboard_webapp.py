import pynput   #其他诸如pymouse,pykeyboard，安装了都不能兼容，在3.8
import time

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
    keyboard = pynput.keyboard.Controller()
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
#键盘侦听
def keyboard_listener():
    keyboard = pynput.keyboard.Controller()
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
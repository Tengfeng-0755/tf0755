######################################################
#外部调用类的例程
#调用侦听
# mouse_obj = mouse_event
# mouse_obj.mouse_listener()
#调用鼠标移动并按键
# mouse_obj.point_set_x = 1268
# mouse_obj.point_set_y = 678
# mouse_obj.botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
# mouse_obj.mouse_point_move()  # 移动到墨侠按钮
# mouse_obj.mouse_click()  # 按下左键

######################################################


import pynput   #其他诸如pymouse,pykeyboard，安装了都不能兼容，在3.8
import time
from enum import Enum

class   mouse_event_mode(Enum):
    MODE_MOVE_EVENT = 1
    MODE_LISTON_EVENT = 2
    MODE_CLICK_EVENT = 3
    MODE_SCROLL_EVENT = 4

class   mouse_click_botton(Enum):
    CLICK_LEFT_BOTTON = 1
    CLICK_RIGHT_BOTTON = 2
    CLICK_MIDDLE_BOTTON = 3


#鼠标事件类
class   mouse_event:
    botton_click = mouse_click_botton.CLICK_LEFT_BOTTON
    point_set_x = 0
    point_set_y = 0
#通用函数
    def on_move(x,y):
        print('Pointer moved to {0}'.format((x,y)))

    def on_click(x,y,button,pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x,y)))

    def on_scroll(x,y,dx,dy):
        print('Scrolled {0} at  {1}'.format('down' if dy < 0 else 'up',(x,y)))

# 鼠标侦听函数
# Collect events until released
    def mouse_listener(self):
        with    pynput.mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()

#  鼠标控制函数

#鼠标点击
#参数x：0，侦听鼠标坐标；1，设置鼠标移动
#参数y,z：鼠标移动的坐标点
    def mouse_click(self):
        ctr = pynput.mouse.Controller()
        if(self.botton_click == mouse_click_botton.CLICK_LEFT_BOTTON):
            ctr.press(pynput.mouse.Button.left)
            ctr.release(pynput.mouse.Button.left)  # 释放左键。
        else:
            ctr.press(pynput.mouse.Button.right)
            ctr.release(pynput.mouse.Button.right)   #释放左键。
#鼠标坐标设置及移动
    def mouse_point_move(self):
        ctr = pynput.mouse.Controller()
        # Read pointer position
        print('The current pointer position is {0}'.format(
            ctr.position))

        # Set pointer position
        ctr.position = (self.point_set_x, self.point_set_y)
        print('Now we have moved it to {0}'.format(
            ctr.position))

        # Move pointer relative to current position
        ctr.move(5, -5)

#模拟滚轮上下滑动
    def mouse_scroll_test(self):
        ctr = pynput.mouse.Controller()
        ctr.scroll(0, 500)
        # 向上滚动50单位。

        ctr.scroll(0, -500)

#封装鼠标操作，这段是采用函数调用的方式，现在不用了
#参数x：0，侦听鼠标坐标；1，设置鼠标移动；2、设置鼠标点击
#参数y,z：鼠标移动的坐标点
# def mouse_call(x,y,z,c):
#     if(x == 0):
#         mouse_listener()
#     elif(x == 1):
#         mouse_point_move(y,z)
#     else:
#         mouse_click(c)

#测试函数，采用调用类的方式。
#鼠标侦听测试函数
def mouse_listen_test():
    mouse_obj = mouse_event
    mouse_obj.mouse_listener(mouse_obj)


#鼠标移位及点击测试函数，可以采用循环调用列表对坐标和打印内容赋值，懒得做
def mouse_press_test():
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

import time
from WebApp.mouse_webapp  import   mouse_event,mouse_click_botton   #调用同一项目下不同目录文件的函数
from enum import Enum

class   mode_type(Enum):
    MODE_XUNMO = 1
    MODE_DOUJIAN = 2
    MODE_SUOYAO = 3

class   sscq_game_run:
#这段是类的属性
    game_name = "sscq自动脚本"
    game_run_ver = "V1.00"
    mode = mode_type.MODE_XUNMO

# 程序信息函数
    def print_program_inf(self):
        print(f'Programer name: {self.game_name}')  # 打印脚本名。
        print(f'Version: {self.game_run_ver}')  # 打印版本。

#这段是类的方法
    def game_run(self):
        if(self.mode == mode_type.MODE_XUNMO):
            game_run_xunmo()
        elif(self.mode == mode_type.MODE_DOUJIAN):
            game_run_doujian()
        elif (self.mode == mode_type.MODE_SUOYAO):
            game_run_suoyao()
        else:
            print("没有可执行代码")

def game_run_xunmo():
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

def game_run_doujian():
    print("没有可执行代码")

def game_run_suoyao():
    print("没有可执行代码")

def game_run_test():
    game_test = sscq_game_run
    game_test.game_name = "sscq自动脚本"
    game_test.game_run_ver = "V1.00"
    game_test.mode = mode_type.MODE_XUNMO
    game_test.print_program_inf(game_test)
    game_test.game_run(game_test)
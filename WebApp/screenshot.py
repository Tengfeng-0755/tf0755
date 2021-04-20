###################################################################
#外部调用类的例程
#截屏的调用，包括全屏截屏和按框截屏
#按全屏截屏
    # srn_shot = screen_shot()
    # srn_shot.mode =screen_shot_mode.MODE_FULLSCREEN
    # screen_shot.screen_shot_run(srn_shot)
#按框截屏
    # box_l = [1,1,1500,1500]
    # screen_shot_box(box_l)
###################################################################

# from PIL import Image
# from PIL import ImageGrab
# import imagehash3
# import tempfile
# import atexit
import os
from enum import Enum

class   screen_shot_mode(Enum):
    MODE_FULLSCREEN = 1
    MODE_BBOX = 2

#使用面向对象的代码进行重构
class   screen_shot:
    mode = screen_shot_mode.MODE_FULLSCREEN
    sharp_list = (0,0,0,0)


    def screen_shot_run(self):
        "Grab the whole screen"
        import pyscreenshot as ImageGrab
        print(os.getcwd())  # 获取文件存储的目录
        if(self.mode == screen_shot_mode.MODE_FULLSCREEN):
            # grab fullscreen
            im = ImageGrab.grab()
            # save image file
            im.save("./SSCQ_screenshot/fullscreen.png")   #怎么打印其保存路径？
        else:
            "Grab the part of the screen"
            # part of the screen
            im = ImageGrab.grab(bbox=self.sharp_list)
            # save image file
            im.save("./SSCQ_screenshot/box.png")


#测试函数
def screen_shot_fullscreen():
    srn_shot = screen_shot()
    srn_shot.mode =screen_shot_mode.MODE_FULLSCREEN
    screen_shot.screen_shot_run(srn_shot)

#算不算个接口？
def screen_shot_box(l=[]):
    srn_shot = screen_shot()
    srn_shot.mode =screen_shot_mode.MODE_BBOX
    # srn_shot.sharp_list = (1, 1, 100, 100)
    srn_shot.sharp_list = l
    screen_shot.screen_shot_run(srn_shot)
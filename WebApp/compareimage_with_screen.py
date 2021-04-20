
import  cv2 #安装了opencv-python，正常了
# import numpy as np

#这里最大的坑，是cv的imread,imwrite是不支持中文的，无论路径还是文件名
def matchImg(imgsrc,imgobj):
    target = cv2.imread(imgsrc)
    template = cv2.imread(imgobj)
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)

    th, tw = template.shape[:2]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if min_val < 0.1:   #90%以上的匹配
        print("min_val", min_val)
        print("max_val", max_val)
        print("min_loc", min_loc)
        print("max_loc", max_loc)
        tl = min_loc
        br = (tl[0] + tw, tl[1] + th)
        cv2.rectangle(target, tl, br, (0, 0, 255), 2)  # tl为左上角坐标，br为右下角坐标，从而画出矩形
        return tl,br
    else:
        return -1

#从比对图中，获得需要点击的按钮位置
def matchpoint_get(imgsrc,imgobj):
    res = matchImg(imgsrc,imgobj)
    if res != -1:
        x3 = res[0]
        y3 = res[1]
        x1,y1 = x3
        x2,y2 = y3
        # x1 = res[0][0]    #另一种不高大上的取值方法
        # x2 = res[1][0]
        # y1 = res[0][1]
        # y2 = res[1][1]
        x = (x1 + x2)//2
        y = (y1 + y2)//2
        print(x,y)

def match_image_test():
    taget_img = "./SSCQ_screenshot/fullscreen.png"
    obj_img = "./SSCQ_screenshot/doujian.png"
    matchpoint_get(taget_img,obj_img)

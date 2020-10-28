import cv2
import os
import platform
import numpy as np

#图像变为以前的一半
def resizeHalf(img_source):
    x,y = img_source.shape[0:2]
    image_des = cv2.resize(img_source, (int(y / 2), int(x / 2)))
    return image_des

# 最近邻插值法缩放
# 缩放到原来的四分之一
def resizeA_quater(img_source):
    image_des = cv2.resize(img_source, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)
    return image_des

#调整为任意尺寸
def resizeAnysize(img_source,desSize):
    image_des = cv2.resize(img_source, desSize)
    return image_des

def resizePic(source,des):
    if os.path.isdir(source):
        sourcePathPic = os.listdir(source)
        for s in sourcePathPic:
            picPath = "{}/{}".format(source,s)
            if platform.system().lower() == 'windows':
                img = cv2.imdecode(np.fromfile(picPath, dtype = np.uint8), 1)
            elif platform.system().lower() == 'linux':
                img = cv2.imread(picPath)
            desSize = (1280,720)
            image_des = resizeAnysize(img,desSize)
            picPath = "{}/{}".format(des, s)
            cv2.imencode('.jpg', image_des)[1].tofile(picPath)  #可能是wndows下采取此方式，防止图片乱码
            #cv2.imwrite(picPath,image_des)

if __name__ == "__main__":
    sourceDic = "F:/pic/source"     #修改原始路径
    destinationDic = "F:/pic/des"      #修改目标路径
    if not os.path.exists(destinationDic):
        os.mkdir(destinationDic)
    resizePic(sourceDic,destinationDic)






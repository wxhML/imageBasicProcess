import cv2
import os
import platform
import numpy as np
import glob
import json
import glob
import shutil
import os
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
            cv2.imencode('.jpg', image_des)[1].tofile(picPath)  #可能是windows下采取此方式，防止图片乱码
            #cv2.imwrite(picPath,image_des)


def batchResizePic(sourcePic,desPic):
    if platform.system().lower() == 'windows':
        img = cv2.imdecode(np.fromfile(sourcePic, dtype=np.uint8), 1)

    elif platform.system().lower() == 'linux':
        img = cv2.imread(sourcePic)
    desSize = (1280, 720)
    image_des = resizeAnysize(img, desSize)
    cv2.imencode('.jpg', image_des)[1].tofile(desPic)  # 可能是windows下采取此方式，防止图片乱码
    # cv2.imwrite(picPath,image_des)

#三层目录
#F:\pic\大兴机场最终素材
#F:\pic\大兴机场最终素材\sss
#F:\pic\大兴机场最终素材\sss\0  图片所在的文件夹

if __name__ == "__main__":
    # sourceDic = "F:/基础测试集(经过测试部人员确定的数据集）"     #修改原始路径
    sourceDic = "F:/pic/大兴机场最终素材"
    sourceDic = "N:/基础测试集"
    sourceDic = "N:/多样车牌测试集"
    sourceDic = "F:/新能源A"


    # sourceDic = "F:/双层黄牌"
    destinationDicS = "G:/dataBase"      #修改目标路径
    destinationDicS = "F:/xintest"   #新能源
    destinationDicS = "F:/yellowPlateTest"      #黄牌测试
    destinationDicS = "F:/新能源B"
    # dataBase = os.listdir(destinationDicS)
    # for singlePath in dataBase:
    #     if singlePath[-4:] != ".zip":
    #         print("G:/dataBase/{}".format(singlePath))



    if not os.path.exists(destinationDicS):
        # os.mkdir(destinationDic)
        os.makedirs(destinationDicS)
    firstDataBases = os.listdir(sourceDic)
    for EveryProvince in firstDataBases:
        # if EveryProvince != "新能源":
        #     continue
        # if EveryProvince != "单层黄牌":
        #     continue
        EveryProvince = sourceDic+"/"+EveryProvince
        singleFilePaths = os.listdir(EveryProvince)
        for singleFile in singleFilePaths:
            # if singleFile != "130_140":
            #     continue
            # if singleFile == "150_160":
            #     break
            singleFile = EveryProvince+"/"+singleFile
            if os.path.isdir(singleFile):
                desPath = singleFile.replace(sourceDic,destinationDicS)
                if not os.path.exists(desPath):
                    os.makedirs(desPath)
                listPic = glob.glob(singleFile+"/*.jpg")
                for singlePic in listPic:
                    destinationDic = singlePic.replace(sourceDic,destinationDicS)
                    print("\n{}".format(destinationDic))
                    # with open(singlePic[:-4]+".json", 'r', encoding='utf-8') as f:
                    #     ret_dic = json.load(f)
                    #     name = ret_dic["plate_0"]["license"]
                    #     destinationDic = destinationDic.split("_")[0] + "_" + destinationDic.split("_")[1] + "_{}.jpg".format(name)

                    batchResizePic(singlePic,destinationDic)






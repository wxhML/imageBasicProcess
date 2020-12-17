#coding=gbk
#coding=utf-8
import json
import glob
import shutil
import os
import platform
import cv2
import numpy as np

from PIL import  ImageFilter
import PIL.Image as pimg

#读取json文件后，将位置信息和标签转化为
def readSingleJson(jsonPath):
    with open(jsonPath, 'r', encoding='utf-8') as f:
                ret_dic = json.load(f)
                name = ret_dic["Plates"][0]["PlateLicense"]
                if name[:2] != "民航":
                    type = ret_dic["Plates"][0]["PlateType"]
                    print(type)
                for index in range(int(ret_dic["Plates"][0]["CharCount"])):
                    cPt0X = ret_dic["Plates"][0]["CharPts"][index]["cPt0X"]
                    cPt0Y = ret_dic["Plates"][0]["CharPts"][index]["cPt0Y"]
                    cPt1X = ret_dic["Plates"][0]["CharPts"][index]["cPt1X"]
                    cPt1Y = ret_dic["Plates"][0]["CharPts"][index]["cPt1Y"]
                    cPt2X = ret_dic["Plates"][0]["CharPts"][index]["cPt2X"]
                    cPt2Y = ret_dic["Plates"][0]["CharPts"][index]["cPt2Y"]
                    cPt3X = ret_dic["Plates"][0]["CharPts"][index]["cPt3X"]
                    cPt3Y = ret_dic["Plates"][0]["CharPts"][index]["cPt3Y"]
                    # print(cPt0X)
                    # print(cPt0Y)
                    # print(cPt1X)
                    # print(cPt1Y)
                    # print(cPt2X)
                    # print(cPt2Y)
                    # print(cPt3X)
                    # print(cPt3Y)

                    minX = cPt2X if cPt0X >cPt2X else cPt0X
                    maxX = cPt3X if cPt3X >cPt1X else cPt1X

                    minY = cPt1Y if cPt0Y > cPt1Y else cPt0Y
                    maxy = cPt2Y if cPt2Y > cPt3Y else cPt3Y
                    # print("")
                    # print(minX)
                    # print(maxX)
                    # print(minY)
                    # print(maxy)

                    x1 = int(minX)
                    y1 = int(minY)
                    w = int(float(maxX) - float(minX))
                    h = int(float(maxy) - float(minY))
                    x2 = x1 + w
                    y2 = y1 + h

                    # print("")
                    # print(x)
                    # print(y)
                    # print(w)
                    # print(h)

                    # if platform.system().lower() == 'windows':
                    #     img = cv2.imdecode(np.fromfile(jsonPath[:-4], dtype = np.uint8), 1)
                    # elif platform.system().lower() == 'linux':
                    #     img = cv2.imread(jsonPath[:-4])
                    # img = pimg.open(os.path.join(img_path, filename))  # 读取对应的图片
                    img = pimg.open(jsonPath[:-4])
                    width, high = img.size
                    trueLabel = name[index]
                    for count in range(5):
                        pass

















if __name__ == "__main__":
    firstFolderPath = "F:/蓝牌标记/车牌标记2-20201106"
    folderList = os.listdir(firstFolderPath)
    for singleFolder in folderList:
        singleFolderPath = "{}/{}".format(firstFolderPath,singleFolder)
        allSigleFolderJson = glob.glob("{}/*.json".format(singleFolderPath))
        for singleJson in allSigleFolderJson:
            readSingleJson(singleJson)






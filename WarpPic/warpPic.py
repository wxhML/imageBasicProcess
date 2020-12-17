import cv2 as cv
import numpy as np
import json
import glob
import shutil
import os

if __name__ == "__main__":
    firstFileFolder = "F:/¾üÅÆ/¹þ¶û±õÃñº½ºÚ/¹þ¶û±õÃñº½ºÚ"
    for folder in os.listdir(firstFileFolder):
        allListJson = glob.glob("{}/{}*.json".format(firstFileFolder,folder))
        for singleJson in allListJson:
            with open(singleJson, 'r', encoding='utf-8') as f:
                ret_dic = json.load(f)
                cPt0X = ret_dic["Plates"][0]["CharPts"][0]["cPt0X"]
                cPt0Y = ret_dic["Plates"][0]["CharPts"][0]["cPt0Y"]
                cPt1X = ret_dic["Plates"][0]["CharPts"][0]["cPt1X"]
                cPt1Y = ret_dic["Plates"][0]["CharPts"][0]["cPt1Y"]
                cPt2X = ret_dic["Plates"][0]["CharPts"][0]["cPt2X"]
                cPt2Y = ret_dic["Plates"][0]["CharPts"][0]["cPt2Y"]
                cPt3X = ret_dic["Plates"][0]["CharPts"][0]["cPt3X"]
                cPt3Y = ret_dic["Plates"][0]["CharPts"][0]["cPt3Y"]
            p1 = np.float32([[cPt0X, cPt0Y], [cPt1X, cPt1Y], [cPt2X, cPt2Y], [cPt3X, cPt3Y]])
            p2 = np.float32([[cPt0X, cPt0Y], [cPt0X+28, cPt0Y], [cPt0X, cPt0Y+28], [cPt0X+28, cPt0Y+28]])
            M = cv.getPerspectiveTransform(p1,p2)
            img = cv.imdecode(np.fromfile(singleJson[:-5], dtype=np.uint8), 0)
            dst = cv.warpPerspective(img, M, (28, 28))




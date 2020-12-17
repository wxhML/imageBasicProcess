import shutil
import os
import json
import glob
#pycharm批量替换 ctrl+R

def isContainChinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False

def accuracy(filePath,saveFile):

    right = 0
    error = 0
    truthLabel = ""
    predictLabel = ""
    index = 0
    flag = False
    errList=[]
    picName = ""
    index1 = 0
    errorPicList = []
    picPath = ""
    distance1 = {}

    with open(filePath, 'r', encoding='gbk') as readFile:  # 按照gbk的编码来读取文件
        for line in readFile.readlines():
            line = line.replace("\n", "")
            if line.find("distance1:") != -1:
                dis = int(line[line.find("distance1:")+10:])
                if dis < 6:
                    num = distance1.get(dis,-1)
                    if num != -1:
                        distance1[dis] = num+1
                    else:
                        distance1[dis] = 1
            if flag:
                predictLabel = line
                if predictLabel.find("民航") != -1 and predictLabel.find("AF") == -1:
                    # print(errorPicList[0])
                    index1 += 1
                    # print(index1)
                    with open(saveFile, 'a+') as fileWrite:
                        fileWrite.write('{} {}'.format(truthLabel, predictLabel) + "\n")
                    # print(picPath)
                    print('{} {}'.format(truthLabel, predictLabel))

                    # picPathJson = picPath + ".json"
                    # shutil.copy(picPath,"G:/errorPic")
                    # shutil.copy(picPathJson, "G:/errorPic")

                if truthLabel == predictLabel:
                # if predictLabel.find("民航")  != -1:
                    right += 1
                    errorPicList.clear()

                    # print("right: {}".format(right))
                    # print('{} {}'.format(truthLabel, predictLabel))
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/right'):
                    #     os.mkdir("F:/pic/大兴机场最终素材/test/right")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/right")
                else:
                    error += 1
                    errorPicList.clear()



                    # picPathJson = picPath +".json";
                    # shutil.move(picPath, "F:/军牌/海川一通--警官学院（含军牌与新武警）/军牌/1/双层错误")
                    # shutil.move(picPathJson, "F:/军牌/海川一通--警官学院（含军牌与新武警）/军牌/1/双层错误")


                    # print("error: {}".format(error))
                    # print('{} {}'.format(truthLabel, predictLabel))
                    # print(picPath)
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/error'):
                    #     os.mkdir("F:/pic/大兴机场最终素材/test/error")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/error")

                flag = False
            if line.find("name:") != -1:
                lizi = line[:line.find("name:")]
                picPath = line[line.find("name:")+5:]
                truthLabel = line.split("_")[-1][:-4]
                if len(truthLabel) < 3 and truthLabel == "":
                    truthLabel = line.split("_")[-2]
                    picName = line[line.find("name:") + 5:]

                if lizi.find("AF") != -1 and truthLabel.find("AF") != -1:
                    pass
                    # shutil.move(picPath, "G:/errorPic")
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/NOAF1'):
                    #         os.mkdirs("F:/pic/大兴机场最终素材/test/NOAF1")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/NOAF1")

                # if lizi.find("A") == -1 or lizi.find("F") == -1 and :
                # if lizi.find("U") != -1:
                # if lizi.find("A") != -1:
                #     if not os.path.exists('F:/pic/大兴机场最终素材/test/SHIBIE1'):
                #         os.mkdir("F:/pic/大兴机场最终素材/test/SHIBIE1")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/SHIBIE1")

                flag = True
                errorPicList.append(picName)
                # print(truthLabel)
                index += 1
                # print(index)
                # if index == 1095:
                #     break
        print("pre: {}".format(right/(right+error)*100))

        print("right: {}".format(right))
        print("error: {}".format(error))

        print("all: {}".format(right+error))
        print(distance1)
def Onlyaccuracy(filePath):
    intMoverightIndex = 0
    intMoveErrorIndex = 0
    intRightFolder = 10
    intErrorFolder = 10
    right = 0
    error = 0
    truthLabel = ""
    predictLabel = ""
    index = 0
    flag = False
    errList=[]
    picName = ""
    index1 = 0
    errorPicList = []
    picPath = ""
    distance1 = {}
    chineseNumber = 0
    firstcharNum =0
    secondCharnum = 0
    EnglishCharNum = 0
    DigitNum = 0
    OtherNum = 0
    firstDigitNum = 0
    lastDigitNum = 0


    with open(filePath, 'r', encoding='gbk') as readFile:  # 按照gbk的编码来读取文件
        for line in readFile.readlines():
            line = line.replace("\n", "")
            # if line.find("name:") != -1:
            #     lizi = line[:line.find("name:")]
            #     picPath = line[line.find("name:") + 5:]
            #     right += 1
            #     if right % 500 == 0:
            #         intRightFolder += 1
            #     pathss = "F:/军牌/多样车牌/双层军牌/right{}".format(intRightFolder+13)
            #     if not os.path.exists(pathss):
            #         os.mkdir(pathss)
            #     shutil.move(picPath, pathss)
            #     shutil.move(picPath+".json", pathss)



            if line.find("distance1:") != -1:
                dis = int(line[line.find("distance1:")+10:])
                num = distance1.get(dis,-1)
                if dis < 5:
                    if num != -1:
                        distance1[dis] = num+1
                    else:
                        distance1[dis] = 1
            if flag:
                predictLabel = line
                if predictLabel.find("民航") != -1 :
                    # print(errorPicList[0])
                    index1 += 1
                    #print(index1)
                    # print(picPath)
                    #print('{} {}'.format(truthLabel, predictLabel))

                    # picPathJson = picPath + ".json"
                    # shutil.copy(picPath,"G:/errorPic")
                    # shutil.copy(picPathJson, "G:/errorPic")

                if truthLabel == predictLabel:
                # if predictLabel.find("民航")  != -1:
                    right += 1
                    if right % 500 == 0:
                        intRightFolder += 1
                    # pathss = "F:/军牌/多样车牌/双层/right{}".format(intRightFolder+3)
                    # if not os.path.exists(pathss):
                    #     os.mkdir(pathss)
                    #
                    # shutil.move(picPath, pathss)
                    # shutil.move(picPath+".json", pathss)

                    errorPicList.clear()
                    # print("right: {}".format(right))
                    # print('{} {}'.format(truthLabel, predictLabel))
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/right'):
                    #     os.mkdir("F:/pic/大兴机场最终素材/test/right")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/right")
                else:
                    error += 1
                    if error % 500 == 0:
                        intErrorFolder += 1
                    if isContainChinese(predictLabel):
                        chineseNumber += 1
                        # pathYellowChar = "F:/军牌/多样车牌/双层/error黄牌或者蓝牌"
                        # if not os.path.exists(pathYellowChar):
                        #     os.mkdir(pathYellowChar)
                        # shutil.move(picPath, pathYellowChar)
                        # shutil.move(picPath + ".json", pathYellowChar)
                    elif truthLabel[0] != predictLabel[0] and truthLabel[1:] == predictLabel[1:]:
                        firstcharNum += 1
                        # pathFirstChar = "F:/军牌/多样车牌/错误的HR_HB/error第一个字符"
                        # if not os.path.exists(pathFirstChar):
                        #     os.mkdir(pathFirstChar)
                        # shutil.copy(picPath, pathFirstChar)
                        # shutil.copy(picPath + ".json", pathFirstChar)
                    elif truthLabel[1] != predictLabel[1] and truthLabel[0] == predictLabel[0] and truthLabel[2:] == predictLabel[2:] :
                        secondCharnum += 1
                        # pathSecondChar = "F:/军牌/多样车牌/错误的HR_HB/error第二个字符"
                        # if not os.path.exists(pathSecondChar):
                        #     os.mkdir(pathSecondChar)
                        # shutil.copy(picPath, pathSecondChar)
                        # shutil.copy(picPath + ".json", pathSecondChar)
                    elif truthLabel[2] != predictLabel[2] and truthLabel[0:2] == predictLabel[0:2] and truthLabel[3:] == predictLabel[3:]:
                        firstDigitNum += 1
                        # pathNumfirstDigitChar = "F:/军牌/多样车牌/双层/error第一个数字字符"
                        # if not os.path.exists(pathNumfirstDigitChar):
                        #     os.mkdir(pathNumfirstDigitChar)
                        # shutil.move(picPath, pathNumfirstDigitChar)
                        # shutil.move(picPath + ".json", pathNumfirstDigitChar)
                    elif truthLabel[0:-1] == predictLabel[0:-1] and truthLabel[-1] != predictLabel[-1]:
                        lastDigitNum += 1
                        # lastNumfirstDigitChar = "F:/军牌/多样车牌/双层/error最后一个数字字符"
                        # if not os.path.exists(lastNumfirstDigitChar):
                        #     os.mkdir(lastNumfirstDigitChar)
                        # shutil.move(picPath, lastNumfirstDigitChar)
                        # shutil.move(picPath + ".json", lastNumfirstDigitChar)
                    elif truthLabel[0:2] == predictLabel[0:2] and truthLabel[2:] != predictLabel[2:]:
                        DigitNum += 1
                        # pathNumChar = "F:/军牌/多样车牌/双层/error数字字符"
                        # if not os.path.exists(pathNumChar):
                        #     os.mkdir(pathNumChar)
                        # shutil.move(picPath, pathNumChar)
                        # shutil.move(picPath + ".json", pathNumChar)
                    elif truthLabel[0:2] != predictLabel[0:2] and truthLabel[2:] == predictLabel[2:]:
                        EnglishCharNum += 1
                        # pathEnglishChar = "F:/军牌/多样车牌/双层/error两个英文字符都错"
                        # if not os.path.exists(pathEnglishChar):
                        #     os.mkdir(pathEnglishChar)
                        # shutil.move(picPath, pathEnglishChar)
                        # shutil.move(picPath + ".json", pathEnglishChar)

                    else:
                        OtherNum += 1
                        # pathotherChar = "F:/军牌/多样车牌/错误的HR_HB/error其他字符"
                        # if not os.path.exists(pathotherChar):
                        #     os.mkdir(pathotherChar)
                        # shutil.move(picPath, pathotherChar)
                        # shutil.move(picPath + ".json", pathotherChar)

                    errorPicList.clear()

                    # picPathJson = picPath +".json";
                    #shutil.move(picPath, "F:/军牌/军车武警车分单双层-已筛选-20201111/军车/双层/2/错误")
                    # shutil.move(picPathJson, "F:/军牌/海川一通--警官学院（含军牌与新武警）/军牌/1/双层错误")
                    # dis = picPath.replace("F:/pic/大兴机场最终素材","F:/pic/大兴机场最终素材 - 副本")
                    # shutil.copy(picPath, "F:/军牌/军车武警车分单双层-已筛选-20201111/军车/双层/错误")

                    # print("error: {}".format(error))
                    # print('{} {}'.format(truthLabel, predictLabel))
                    # print(picPath)
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/error'):
                    #     os.mkdir("F:/pic/大兴机场最终素材/test/error")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/error")

                flag = False
            if line.find("name:") != -1:
                lizi = line[:line.find("name:")]
                picPath = line[line.find("name:")+5:]
                truthLabel = line.split("_")[-1][:-4]
                if len(truthLabel) < 3 and truthLabel == "":
                    truthLabel = line.split("_")[-2]
                    picName = line[line.find("name:") + 5:]

                if lizi.find("AF") != -1 and truthLabel.find("AF") != -1:
                    pass
                    # shutil.move(picPath, "G:/errorPic")
                    # if not os.path.exists('F:/pic/大兴机场最终素材/test/NOAF1'):
                    #         os.mkdirs("F:/pic/大兴机场最终素材/test/NOAF1")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/NOAF1")

                # if lizi.find("A") == -1 or lizi.find("F") == -1 and :
                # if lizi.find("U") != -1:
                # if lizi.find("A") != -1:
                #     if not os.path.exists('F:/pic/大兴机场最终素材/test/SHIBIE1'):
                #         os.mkdir("F:/pic/大兴机场最终素材/test/SHIBIE1")
                    # shutil.move(picName, "F:/pic/大兴机场最终素材/test/SHIBIE1")

                flag = True
                errorPicList.append(picName)
                # print(truthLabel)
                index += 1
                # print(index)
                # if index == 1095:
                #     break
        print("pre: {}".format(right/(right+error)*100))
        print("yellowPlate: {}".format(chineseNumber / (right + error) * 100))
        print("FirstPlate: {}".format( firstcharNum/ (right + error) * 100))
        print("secondPlate: {}".format(secondCharnum / (right + error) * 100))
        print("EnglishPlate: {}".format(EnglishCharNum / (right + error) * 100))
        print("firstDigit: {}".format(firstDigitNum / (right + error) * 100))
        print("digitPlate: {}".format(DigitNum / (right + error) * 100))
        print("lastPlate: {}".format(lastDigitNum / (right + error) * 100))
        print("otherPlate: {}".format(OtherNum / (right + error) * 100))

        print("right: {}".format(right))
        print("error: {}".format(error))
        print("all: {}".format(right+error))
        print(distance1)
        disPercent = {}
        all = 0
        allLEN = 0
        for (key,value) in  distance1.items():
            all += value
            allLEN += value*key
        for (key,value) in  distance1.items():
            disPercent[key] = value /all*100
        #print("pingjun:{}".format(allLEN/all))

        # print(disPercent)
        dicp = sorted(disPercent.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

        #print(dicp)
        #print(len(dicp))
        for i in dicp:
            # print(i)
            char = str(i).split(",")[0][1:]

            num = str(i).split(",")[1][:-1]
            num = float(num)

            # num = int(i).split(",")[1][:]
            #print(str(char)+": ",end="")
            # print(type(num))
            # print(num)
            #print("%.3f%%" % (num))

            # print(type(i))


        # for (key,value) in dicp.items():
        #      print(str(key)+": ",end="")
        #      print("%.3f" % (value))


def testAccuaracy(filePath):

    intRightFolder = 10

    right = 0
    error = 0
    truthLabel = ""

    index = 0
    flag = False

    picName = ""
    index1 = 0
    errorPicList = []

    distance1 = {}

    minghanghei = 0
    minhang = 0
    hanzi  = 0
    base = 0
    hei = 0
    #with open(filePath, 'r', encoding='gbk') as readFile:  # 按照gbk的编码来读取文件
    with open(filePath, 'r', encoding='utf-8') as readFile:  # 按照gbk的编码来读取文件
        for line in readFile.readlines():
            line = line.replace("\n", "")

            if line.find("distance1:") != -1:
                dis = int(line[line.find("distance1:") + 10:])
                num = distance1.get(dis, -1)
                if dis < 5:
                    if num != -1:
                        distance1[dis] = num + 1
                    else:
                        distance1[dis] = 1
            if flag:
                predictLabel = line
                if predictLabel.find("民航") != -1:
                    index1 += 1
                if truthLabel == predictLabel:
                    # if predictLabel.find("民航")  != -1:
                    right += 1
                    if right % 500 == 0:
                        intRightFolder += 1
                    errorPicList.clear()
                else:
                    if predictLabel.find("民航黑") != -1:
                        #print("{} {}".format(predictLabel,picPath))
                        minghanghei += 1
                    elif predictLabel.find("民航") != -1:
                        #print("{} {}".format(predictLabel, picPath))
                        minhang += 1
                    elif predictLabel.find("黑") == -1 and predictLabel == "kong":
                        print("{} {}".format(predictLabel, picPath))
                        hanzi += 1
                    elif predictLabel.find("黑") != -1:
                        #print("{} {}".format(predictLabel, picPath))
                        hei += 1
                    else:
                        print("{} {}".format(predictLabel, picPath))
                        base += 1
                    error += 1
                    errorPicList.clear()
                flag = False
            if line.find("name:") != -1:
                lizi = line[:line.find("name:")]
                picPath = line[line.find("name:") + 5:]
                truthLabel = line.split("_")[-1][:]
                if len(truthLabel) < 3 and truthLabel == "":
                    truthLabel = line.split("_")[-2]
                    picName = line[line.find("name:") + 5:]

                if lizi.find("AF") != -1 and truthLabel.find("AF") != -1:
                    pass


                flag = True
                errorPicList.append(picName)

                index += 1

        print("pre: {}".format(right / (right + error) * 100))
        print("right: {}".format(right))
        print("error: {}".format(error))
        print("all: {}".format(right + error))
        print("minghanghei: {} {} {}".format(minghanghei,minghanghei / (right + error) * 100,minghanghei/error*100))
        print("minghang: {} {} {}".format(minhang, minhang / (right + error) * 100, minhang / error * 100))
        print("hanzi: {} {} {}".format(hanzi, hanzi / (right + error) * 100, hanzi / error * 100))
        print("hei: {} {} {}".format(hei, hei / (right + error) * 100, hei / error * 100))
        print("basePlate: {} {} {}".format(base, base / (right + error) * 100, base / error * 100))

if __name__ == "__main__":
    # picList = os.listdir("G:/dataBase")
    # for filePath in picList:
    #     path = "F:/dataBase/" + filePath
    #     sourceDir = "G:/dataBase/" + filePath
    #     if not os.path.exists(path):
    #         os.mkdir(path)
    #     lastDir = os.listdir(sourceDir)
    #     for last in lastDir:
    #         paths = path + "/" + last
    #         if not os.path.exists(paths):
    #             os.mkdir(paths)
    # print("rm原版: ")
    # Onlyaccuracy("../rm原版/rm原版.txt")
    # print("rm新版: ")
    # Onlyaccuracy("../新版rm/新版rm.txt")
    # print("rm1新版: ")
    # Onlyaccuracy("../新版rm1/新版rm1.txt")
    #Onlyaccuracy("../新版rm1/result_daxin.txt")
    #Onlyaccuracy("../result_daxin_modifydaxin第一版.txt")
    # Onlyaccuracy("../新版rmOne/result_daxin.txt")
    # Onlyaccuracy("../老版RMone/result_daxin.txt")
    #Onlyaccuracy("../新版rmOne/result_junpai1.txt")


    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWFour.txt")
    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWThree.txt")
    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWThree1.txt")
    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWTwo.txt")
    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWOne.txt")
    # Onlyaccuracy("../test军牌/result_junpai_averageGapAndAverageWZero.txt")
    # Onlyaccuracy("../test军牌/result_junpai_onlyShieldYellowPlate.txt")
    # Onlyaccuracy("../test军牌/result_junpai_onlyNoShieldYellowPlate.txt")
    # Onlyaccuracy("../test军牌/result_junpai_HR_HB.txt")

    # num = 0
    # indexFile = 0
    # firstFile = os.listdir("F:/军牌/多样车牌/双层军牌")
    # for sigleFolderPath in firstFile:
    #     FolderPath = "F:/军牌/多样车牌/双层军牌/{}".format(sigleFolderPath)
    #     alljpgList = glob.glob("{}/*.jpg".format(FolderPath))
    #     indexFileNum = 0
    #     for singleJpg in alljpgList:
    #         if singleJpg.split("\\")[-1].split("_")[-1][0:2] == "HR" or singleJpg.split("\\")[-1].split("_")[-1][0:2] == "HB":
    #             num += 1
    #             print(num)
    #             if num % 500 == 0:
    #                 indexFile += 1
    #             pathPicHB_HR = "F:/军牌/多样车牌/HR_HB/NUM{}".format(indexFile)
    #             if not os.path.exists(pathPicHB_HR):
    #                 os.mkdir(pathPicHB_HR)
    #             shutil.copy(singleJpg, pathPicHB_HR)  # 复制并重新命名图片
    #             shutil.copy(singleJpg + ".json", pathPicHB_HR)  # 复制并重新命名json


    # print("#############################")
    # Onlyaccuracy("../test军牌/result_junpai_NOmodify.txt")
    # print("#############################")
    # Onlyaccuracy("../test军牌/result_junpai_NOmodifyALL.txt")
    # print("#############################")
    # Onlyaccuracy("../test军牌/result_junpai_modify.txt")
    # print("#############################")
    # Onlyaccuracy("../test军牌/result_junpai_modifyALL.txt")
    #testAccuaracy("../test军牌/result_testHEB.txt")
    #testAccuaracy("../test军牌/test_resultdaxin.txt")

    #testAccuaracy("../test军牌/result_daxin.txt")

    #testAccuaracy("../test军牌/test_resultdaxin.txt")


    #testAccuaracy("../test军牌/result_testHEB112.txt")
    # testAccuaracy("../test军牌/result_testHEB1123.txt")
    # testAccuaracy("../test军牌/result_testHEB11234.txt")
    # testAccuaracy("../test军牌/result_testHEB112345.txt")
    #testAccuaracy("../test军牌/result_testHEBR900.txt")
    #testAccuaracy("../test军牌/result_testHEBRM.txt")
    # testAccuaracy("../test军牌/result_testHEBRX.txt")
    #testAccuaracy("../test军牌/test_resultBaseRX.txt")
    #testAccuaracy("../test军牌/test_resultXNY.txt")
    #testAccuaracy("../test军牌/result_heilongjiang.txt")
    testAccuaracy("../test军牌/test_resultYellowPlate.txt")


    # Onlyaccuracy("../test军牌/result_junpai_z.txt")
    # accuracy("../新版rm/新版rm.txt","../新版rm/minghang.txt")
    # accuracy("../rm原版/rm原版.txt","../rm原版/minghang.txt")

    # accuracy("../新版rm/compare.txt","../新版rm/error.txt")
    # accuracy("../rm原版/compare.txt","../rm原版/error.txt")

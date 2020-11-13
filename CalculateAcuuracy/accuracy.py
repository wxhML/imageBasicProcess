import shutil
import os
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
                    print(index1)
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
    Onlyaccuracy("../新版rmOne/result_daxin.txt")
    Onlyaccuracy("../老版RMone/result_all.txt")

    # accuracy("../新版rm/新版rm.txt","../新版rm/minghang.txt")
    # accuracy("../rm原版/rm原版.txt","../rm原版/minghang.txt")

    # accuracy("../新版rm/compare.txt","../新版rm/error.txt")
    # accuracy("../rm原版/compare.txt","../rm原版/error.txt")

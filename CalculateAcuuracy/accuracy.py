import shutil
def accuracy(filePath):
    right = 0
    error = 0
    truthLabel = ""
    predictLabel = ""
    index = 0
    flag = False
    errList=[]
    picName = ""
    with open(filePath, 'r', encoding='gbk') as readFile:  # 按照gbk的编码来读取文件
        for line in readFile.readlines():
            line = line.replace("\n", "")
            if flag:
                predictLabel = line
                if truthLabel == predictLabel:
                    right += 1
                    shutil.move(picName, "F:/pic/大兴机场最终素材/test/right")
                else:
                    error += 1
                    shutil.move(picName, "F:/pic/大兴机场最终素材/test/right")
                print(truthLabel)
                print(predictLabel)
                flag = False
            if line.find("name:") != -1:
                truthLabel = line.split("_")[-1][:-4]
                picName = line[line.find("name:")+5:]


                flag = True
                # print(truthLabel)
                index += 1
                # print(index)
                if index == 1095:
                    break
        print("pre: {}".format(right/(right+error)*100))
        print("right: {}".format(right))
        print("error: {}".format(error))
        print("all: {}".format(right+error))


if __name__ == "__main__":
    accuracy("../result_daxin_modify0.txt")
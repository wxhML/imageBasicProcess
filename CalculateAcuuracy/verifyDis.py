#coding=gbk

def calDis(path):
    standardDis = 0
    unstandard = 0
    middleStard = 0
    with open(path, 'r', encoding='gbk') as readFile:  # 按照gbk的编码来读取文件
        for line in readFile.readlines():
            line = line.replace("\n", "")
            lineList = line.split(" ")
            sum = 0
            for num in range(14,22,2):
                sum += int(lineList[num])
            average = int(sum/4)
            sumGap = 0
            for num in range(24,30,2):
                sumGap += int(lineList[num])
            averageGap = int(sumGap/3)
            if (averageGap ==  int(lineList[22]) and average == int(lineList[12])) or (abs(averageGap -int(lineList[22]))==1 and (average == int(lineList[12]))) \
                    or (averageGap ==  int(lineList[22]) and abs(average-int(lineList[12]))==1) or (abs(averageGap -int(lineList[22]))<=5 and abs(average-int(lineList[12]))<=5 ):
                standardDis += 1

            else:
                unstandard += 1
    print("standardDis: {}".format(standardDis))
    print("unstandardDis: {}".format(unstandard))
    print("proportion: {}".format(standardDis/(standardDis+unstandard)))






if __name__ == "__main__":
    calDis("../test军牌/getDis0.txt")
import os
import shutil
import glob
import cv2

# 符号	描述
# %s	格式化字符串
# %d	格式化整数
# %f	格式化浮点数字，可指定小数点后的精度
# %c	格式化字符及其ASCII码
# %u	格式化无符号整型
# %o	格式化无符号八进制数
# %x	格式化无符号十六进制数
# %X	格式化无符号十六进制数（大写）
# %e	用科学计数法格式化浮点数
# %E	作用同%e，用科学计数法格式化浮点数
# %g	%f和%e的简写
# %G	%f 和 %E 的简写
# %p	用十六进制数格式化变量的地址

def getAllPicPath(path):
    files_txts = os.listdir(path)
    sigle_dir_pics  = []
    for files_txt in files_txts:
        if files_txt == "all.txt":
            continue
        with open(path+"/"+files_txt, 'r', encoding='utf-8') as readFile:
            single_txt_pics=[]
            for line in readFile.readlines():
                single_txt_pics.append(line.replace('\n',""))
            sigle_dir_pics+=single_txt_pics
            print("%s num %d"%(files_txt,len(single_txt_pics)))
    print("%s 总的 num %d"%(path,len(sigle_dir_pics)))
    return sigle_dir_pics
def movpicName(sourceList,despath):
    for filePath in sourceList:
      if filePath.find("民航") != -1:
        shutil.move(filePath,despath)
        #shutil.copy(filePath,dstPath)
        copyPic = os.listdir(despath)

def movePic(sourceList,dstPath):
    num = 0
    for filePath in sourceList:
        num+=1
        # image = cv2.imread(filePath)
        # # print(item)
        # try:
        #     cv2.imshow('img', image)  # 若能show, 则表示无误；若图片有问题这里会有error
        # except:
        #     print('' + 'have problem!')
        #     pass

        print("num :%d %s"%(num,filePath))
        shutil.move(filePath,dstPath)

        #shutil.copy(filePath,dstPath)

    copyPic = os.listdir(dstPath)
    print(len(copyPic))

def getPicFile(file):
    
    with open(file, 'r', encoding='gbk') as readFile:  #按照gbk的编码来读取文件
    #with open(file, 'r', encoding='utf-8') as readFile:
        single_txt_pics = []
        for line in readFile.readlines():
            single_txt_pics.append(line.replace('\n', ""))

        return single_txt_pics


if __name__=="__main__":
    all_pic = []
    all_dir =[]  #原始图片存放的路径

    allList =glob.glob("F:/pic/大兴/*.jpg")
    movpicName(allList,"F:/pic/大兴机场素材1")

    # allMovePic = getPicFile("./pic.txt")  #获取txt中的文件路径
    # dstPath = "F:/pic/moveLast"        #建立存放移动的目录
    # if not (os.path.exists(dstPath)):  #判断一个文件是否存在 os.path.isdir()函数来判断路径是否为目录。
    #     os.mkdir(dstPath)
    #
    # # for single_dir in all_dir:
    # #     all_pic+=getAllPicPath(single_dir)
    # # print(len(all_pic))
    #
    # movePic(allMovePic,dstPath)






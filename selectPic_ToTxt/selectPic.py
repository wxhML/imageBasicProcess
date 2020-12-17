import shutil
def select(filepath,des):
    selectList = []
    with open(filepath, 'r', encoding='gbk') as readFile:  #按照gbk的编码来读取文件
        flag = False
        for line in readFile.readlines():
            line = line.replace("\n","")
            if line.startswith("lizi:"):
                if line.find("AF") == -1:
                    flag = True
                    shutil.move(line.split("___")[-1][5:], "F:/pic/大兴/test/框错误")

            # if flag == True:
            #     if line.startswith("name:"):
            #         selectList.append(line[5:])
            #         shutil.move(readFile[5:], "F:/pic/大兴/test/框错误")  #直接move，no copy
            #         flag = False
    print(len(selectList))

if __name__ == "__main__":
    select("../result_daxin_modify0.txt", "")
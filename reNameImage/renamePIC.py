import os
if __name__ == "__main__":
    with open("F:/pic/result_daxin_modify.txt", 'r') as readFile:
        single_txt_pics = []
        num = 0
        index = 1073
        for line in readFile.readlines():
            num += 1
            single_txt_pics.append(line.replace('\n',""))

            if num==2:
                source = single_txt_pics[0]
                # des = "F:/pic/moveLast/{}_{}.jpg".format(index, single_txt_pics[1])
                des = "f:/pic/大兴/{}_{}.jpg".format(index,single_txt_pics[1])
                if single_txt_pics[1]:
                    if single_txt_pics[1][0] == "民":
                        des = "f:/pic/大兴/民航/{}_{}.jpg".format(index, single_txt_pics[1])
                num = 0
                os.rename(source, des)
                single_txt_pics.clear()
                index += 1





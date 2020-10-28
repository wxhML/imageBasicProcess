import os

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False

# ret1 = is_chinese("刘亦菲")

def getpic_name(file_path_first):
    path = file_path_first
    files= os.listdir(path)
    for filename in files:
        path_txt_name = "F:/pic/" + filename+".txt"
        with open(path_txt_name, 'w', encoding='utf-8') as writer:
            sub_path = path+"/"+filename
            if os.path.isdir(sub_path):
                file_subs = os.listdir(sub_path)
                for file_sub in file_subs:
                    sub1_path = sub_path+"/" + file_sub
                    if file_sub[-4:] == ".jpg":
                        pic_path = sub1_path+"\n"
                        print(sub1_path)
                        writer.write(pic_path)
                    if os.path.isdir(sub1_path):
                        pic_names = os.listdir(sub1_path)
                        for pic_name in pic_names:
                            if pic_name[-4:] == ".jpg":
                                pic_path = sub1_path +"/" + pic_name + "\n"
                                print(sub1_path +"/" + pic_name)
                                writer.write(pic_path)
                            sub_three = sub1_path + "/" + pic_name
                            if os.path.isdir(sub_three):
                                three_dirs = os.listdir(sub_three)
                                for three_dir in three_dirs:
                                    if three_dir[-4:] == ".jpg":
                                        three_dir_list = three_dir.split("_")
                                        if len(three_dir_list[0]) == 8:
                                            print(sub_three + "/" + three_dir)
                                            pic_path = sub_three + "/" + three_dir + "\n"
                                            writer.write(pic_path)
def getEveryProvinceNum(file_path_first):
    path = file_path_first
    path_txt_name = "F:/pic/evertProvice.txt"
    files= os.listdir(path)
    with open(path_txt_name, 'w', encoding='utf-8') as writer:
        for filename in files:
            num = 0
            province = filename +" number: "
            sub_path = path+"/"+filename
            if os.path.isdir(sub_path):
                file_subs = os.listdir(sub_path)
                for file_sub in file_subs:
                    sub1_path = sub_path+"/" + file_sub
                    if file_sub[-4:] == ".jpg":
                        num += 1
                    if os.path.isdir(sub1_path):
                        pic_names = os.listdir(sub1_path)
                        for pic_name in pic_names:
                            if pic_name[-4:] == ".jpg":
                                num += 1
                            sub_three = sub1_path + "/" + pic_name
                            if os.path.isdir(sub_three):
                                three_dirs = os.listdir(sub_three)
                                for three_dir in three_dirs:
                                    if three_dir[-4:] == ".jpg":
                                       num+=1
            print(province + str(num))
            write_data = province + str(num) +"\n"
            writer.write(write_data)

def getNewEnergy_name(data,file_path_first):
    path = file_path_first
    files= os.listdir(path)
    path_txt_name_num = "F:/pic/新能源" + data+ "/all" + ".txt"
    all_num = 0
    with open(path_txt_name_num, 'w', encoding='utf-8') as Numwriter:
        for filename in files:
            num = 0
            path_txt_name = "F:/pic/新能源"+ data + "/"+ filename+".txt"
            with open(path_txt_name, 'w', encoding='utf-8') as writer:
                sub_path = path+"/"+filename
                if os.path.isdir(sub_path):
                    file_subs = os.listdir(sub_path)
                    for file_sub in file_subs:
                        sub1_path = sub_path+"/" + file_sub
                        if file_sub[-4:] == ".jpg":
                            subList = file_sub.split("_")
                            if len(subList[0]) == 8 and is_chinese(subList[0]) and (subList[0][2] =="D" or subList[0][2] =="F"):
                                pic_path = sub1_path + "\n"
                                num += 1
                                all_num += 1
                                print(sub1_path)
                                writer.write(pic_path)
                        if os.path.isdir(sub1_path):
                            pic_names = os.listdir(sub1_path)
                            for pic_name in pic_names:
                                if pic_name[-4:] == ".jpg":
                                    pic_List = pic_name.split("_")
                                    if len(pic_List[0]) == 8 and is_chinese(pic_List[0])and (pic_List[0][2] =="D" or pic_List[0][2] =="F"):
                                        pic_path = sub1_path +"/" + pic_name + "\n"
                                        print(sub1_path +"/" + pic_name)
                                        num += 1
                                        all_num += 1
                                        writer.write(pic_path)
                                sub_three = sub1_path +"/" + pic_name
                                if os.path.isdir(sub_three):
                                    three_dirs = os.listdir(sub_three)
                                    for three_dir in three_dirs:
                                        if three_dir[-4:] == ".jpg":
                                            three_dir_list = three_dir.split("_")
                                            if len(three_dir_list[0]) == 8 and is_chinese(three_dir_list[0])and (three_dir_list[0][2] =="D" or three_dir_list[0][2] =="F"):
                                                print(sub_three + "/" + three_dir)
                                                pic_path = sub_three + "/" + three_dir + "\n"
                                                num += 1
                                                all_num += 1
                                                writer.write(pic_path)
            Numwriter.write(filename+" num: " + str(num)+"\n")
        Numwriter.write("总的 num: " + str(all_num) + "\n")


# file_path_first = "Z:/01_R Series/03_R_Source/202007"
# data = "202007"
file_path_first = "W:/01_R_Series/03_R_Source/202008"
data = "202008"

# getpic_name(file_path_first)
# getEveryProvinceNum(file_path_first)
getNewEnergy_name(data,file_path_first)
import json
import glob
import shutil
import os

# data = {
#     'name': 'pengjunlee',
#     'age': 32,
#     'vip': True,
#     'address': {'province': 'GuangDong', 'city': 'ShenZhen'}
# }
# # 将 Python 字典类型转换为 JSON 对象
# json_str = json.dumps(data)
# print(
#     json_str)  # 结果 {"name": "pengjunlee", "age": 32, "vip": true, "address": {"province": "GuangDong", "city": "ShenZhen"}}
#
# # 将 JSON 对象类型转换为 Python 字典
# user_dic = json.loads(json_str)
# print(user_dic['address'])  # 结果 {'province': 'GuangDong', 'city': 'ShenZhen'}
#
# # 将 Python 字典直接输出到文件
# with open('pengjunlee.json', 'w', encoding='utf-8') as f:
#     json.dump(user_dic, f, ensure_ascii=False, indent=4)
#
# # 将类文件对象中的JSON字符串直接转换成 Python 字典
# allList =glob.glob("F:/大兴机场新车牌10月-已完成-已检查/*.json")
# index = 10000
# for jsonFile in allList:
#     picFile = jsonFile[:-4]
#     with open(jsonFile, 'r', encoding='utf-8') as f:
#         ret_dic = json.load(f)
#         name = ret_dic["Plates"][0]["PlateLicense"]
#         # shutil.move(filePath, dstPath)
#         path = "F:/dd/正确大兴机场/{}_{}.jpg".format(index,name)
#         os.rename(picFile, path)
#         index += 1


#目录带多个文件夹的
# path = "F:/军牌/军车武警车标记-已标记-20201113"
# FirstList = os.listdir(path)

FirstList = ["F:/军牌/哈尔滨机场民航车牌-广州科灵-已标记-20201125"]
index = 0
dicttype = {}
disPath = "F:/军牌/多样车牌/"
disPathPart1 = "F:/军牌/"
disPathPart2 = "哈尔滨民航黑"

# sourcePath = "C:/Users/lxh/Desktop/wrong"
sourcePath = "C:/Users/lxh/Desktop/right"
allPic = glob.glob("{}/*.jpg".format(sourcePath))
FileIndex = 20
for singlePic in allPic:
    p1= singlePic.split("\\")[-1][0]
    p2 = singlePic.split("\\")[-1][2:]
    newP = "F:/军牌/哈尔滨民航黑/" + p1 + "_哈尔滨民航黑/" + p2
    if index % 500 == 0:
        disPathN = "{}{}_{}".format(disPathPart1, FileIndex, disPathPart2)
        FileIndex += 1
    if not (os.path.exists(disPathN)):  # 判断一个文件是否存在 os.path.isdir()函数来判断路径是否为目录。
        os.mkdir(disPathN)
    lastPathPic = "{}/{}".format(disPathN, p2)
    lastPathjson = "{}/{}.json".format(disPathN, p2)
    print(lastPathPic)
    print(lastPathjson)
    shutil.copy(newP,lastPathPic)   #复制并重新命名图片
    shutil.copy(newP+".json", lastPathjson)  # 复制并重新命名json
    index += 1




# for FirstFolder in FirstList:
#     print(FirstFolder)
#     #FirstFolderPath = "{}/{}".format(path,FirstFolder)
#     FirstFolderPath = "{}".format(FirstFolder)
#     allListJson = glob.glob("{}/*.json".format(FirstFolderPath))
#     FileIndex = 0
#     for singleJson in allListJson:
#         with open(singleJson, 'r', encoding='utf-8') as f:
#             ret_dic = json.load(f)
#             name = ret_dic["Plates"][0]["PlateLicense"]
#             if name[:3] == "民航黑":
#                 type = ret_dic["Plates"][0]["PlateType"]
#                 picFile = singleJson[:-5]
#                 jsonFile = picFile +".json"
#                 print(picFile)
#                 print(jsonFile)
#                 if index % 500 == 0:
#                     disPathN = "{}{}_{}".format(disPathPart1,FileIndex,disPathPart2)
#                     FileIndex += 1
#                 if not (os.path.exists(disPathN)):  #判断一个文件是否存在 os.path.isdir()函数来判断路径是否为目录。
#                     os.mkdir(disPathN)
#                 lastPathPic = "{}/{}_{}.jpg".format(disPathN,index, name)
#                 lastPathjson = "{}/{}_{}.jpg.json".format(disPathN, index, name)
#
#                 shutil.copy(picFile,lastPathPic)   #复制并重新命名图片
#                 shutil.copy(jsonFile, lastPathjson)  # 复制并重新命名json
#
#
#
#                 print(index)
#                 index += 1
























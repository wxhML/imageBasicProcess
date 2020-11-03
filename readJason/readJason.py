import json
import glob
import shutil
import os

data = {
    'name': 'pengjunlee',
    'age': 32,
    'vip': True,
    'address': {'province': 'GuangDong', 'city': 'ShenZhen'}
}
# 将 Python 字典类型转换为 JSON 对象
json_str = json.dumps(data)
print(
    json_str)  # 结果 {"name": "pengjunlee", "age": 32, "vip": true, "address": {"province": "GuangDong", "city": "ShenZhen"}}

# 将 JSON 对象类型转换为 Python 字典
user_dic = json.loads(json_str)
print(user_dic['address'])  # 结果 {'province': 'GuangDong', 'city': 'ShenZhen'}

# 将 Python 字典直接输出到文件
with open('pengjunlee.json', 'w', encoding='utf-8') as f:
    json.dump(user_dic, f, ensure_ascii=False, indent=4)

# 将类文件对象中的JSON字符串直接转换成 Python 字典
allList =glob.glob("F:/大兴机场新车牌10月-已完成-已检查/*.json")
index = 10000
for jsonFile in allList:
    picFile = jsonFile[:-4]
    with open(jsonFile, 'r', encoding='utf-8') as f:
        ret_dic = json.load(f)
        name = ret_dic["Plates"][0]["PlateLicense"]
        # shutil.move(filePath, dstPath)
        path = "F:/dd/正确大兴机场/{}_{}.jpg".format(index,name)
        os.rename(picFile, path)
        index += 1











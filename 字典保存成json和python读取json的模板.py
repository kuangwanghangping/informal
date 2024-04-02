# import json
# import os
#
# # 要保存的字典数据
# data = {"key1": "value1", "key2": "value2", "key3": "value3"}
#
# # 指定保存文件的完整路径
# desktop_path = r'C:\Users\Administrator\Desktop'
# file_path = os.path.join(desktop_path, "data.json")
#
# # 将字典保存为 JSON 文件
# with open(file_path, "w") as file:
#     json.dump(data, file)
#
# print("文件已保存到桌面:", file_path)



import json
import os

# 指定要读取的文件路径
desktop_path = r'C:\Users\Administrator\Desktop'
file_path = os.path.join(desktop_path, "data.json")

# 读取 JSON 文件并解析成字典格式
with open(file_path, "r") as file:
    data = json.load(file)

# 打印读取的字典数据
print("读取的字典数据:", type(data))

"""
演示字典的常用操作
"""
my_dict = {"周杰伦": 99, "林俊杰": 88, "刘德华": 77}

# 新增元素
my_dict["狂魔哥"] = 2
print(f"字典经过新增元素后，结果为：{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新元素后，结果为：{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果是{my_dict}，周杰伦的考试成绩是：{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# 获取全部的Key
my_dict = {"周杰伦": 99, "林俊杰": 88, "刘德华": 77}
keys = my_dict.keys()
print(f"字典的全部Keys是：{keys}")

# 遍历字典
# 方式1：通过获取全部的Key来遍历
for key in keys:
    print(f"1:字典的Key是：{key},字典的value是：{my_dict[key]}")
# 方式2：直接对字典进行for循环，每次循环直接得到Key
for key in my_dict:
    print(f"2:字典的Key是：{key},字典的value是：{my_dict[key]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")

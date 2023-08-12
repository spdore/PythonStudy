"""
演示以数据容器的角色，学习字符串的相关操作
"""
my_str = "itheima and itcast"  # 字符串不支持修改
# 通过下标索引取值
value = my_str[2]
value1 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是：{value}，取下标为-16的元素，值是：{value1}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and的下标，其下标为{value}")

# replace方法
new_my_str = my_str.replace("it", "666")
print(new_my_str)  # 字符串内容替换

# split方法
my_str = "hello python it 666"
my_str_list = my_str.split(" ")  # 以空格切分字符串存入my_str_list列表当中
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是{type(my_str_list)}")

# strip方法
my_str = "     123hello python it 666 "
print(my_str.strip())  # 去除字符串的头尾空格与回车换行符
new_my_str = my_str.strip()
print(new_my_str.strip("123"))  # 去除指定头部字符

# 统计字符串中某字符的出现次数 count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")

# 统计字符串的长度
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")

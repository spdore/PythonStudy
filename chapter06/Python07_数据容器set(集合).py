"""
演示数据容器聚合的使用
"""

# 集合是无序的，不支持下标索引访问

# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima"}
my_set_empty = set()  # 定义空集合
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")  # 集合去重，集合内容不许重复
print(f"my_set_empty的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")

# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除元素后的结果是：{my_set}")

# 随机取出一个元素
element = my_set.pop()
print(f"my_set随机取出一个元素是：{element}")

# 清空集合
my_set.clear()
print(f"清空集合后的结果是：{my_set}")

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)  # set1有而set2没有的内容
print(f"set1与set2取差集的结果是：{set3}")
print(f"取差集后原有set1的内容：{set1}")
print(f"取差集后原有set2的内容：{set2}")

# 消除两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)  # 在set1内，删除与set2相同的元素
print(f"消除差集后，set1的结果是：{set1}")  # set1被修改
print(f"消除差集后，set2的结果是：{set2}")  # set2无变化

# 两个集合合并为一个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"合并set1和set2的结果是：{set3}")  # 集合内没有重复元素

# 统计集合的元素数量len()
set1 = {1, 2, 3, 4, 5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")

# 集合的遍历
# 集合不支持下标索引，不能使用while循环
# 可以使用for循环
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有：{element}")

"""
演示数据容器之：list列表的常用操作
"""
mylist = ["ittest", "itheima", "python"]
# 1.1 查找某元素在列表内的下标索引
index = mylist.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")

# 1.2 如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下标索引值是：{index}")

# 2. 修改特定下标索引的值
mylist[0] = "传智教育"
print(f"列表被修改元素值后，结果是{mylist}")

# 3. 在指定下标位置插入新元素
mylist.insert(1, "best")
print(f"列表传入元素后，结果是{mylist}")  # 在1位置插入元素

# 4. 在列表的尾部追加”单个“新元素
mylist.append("黑马程序员")  # append追加单个
print(f"列表再追加了元素后，结果是：{mylist}")

# 5. 在列表的尾部追加“一批”新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)  # extend追加一批
print(f"列表在追加了一个新的列表后，结果是：{mylist}")

# 6. 删除指定下标索引的元素（2种方式）
mylist = ["ittest", "itheima", "python"]

# 6.1 del 列表[下标]
del mylist[2]
print(f"删除结果后，列表元素是{mylist}")

# 6.2 列表.pop(下标)
mylist = ["ittest", "itheima", "python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后，列表元素是{mylist}，取出的元素是{element}")

# 7. 删除某元素在列表中的第一个匹配项
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
mylist.remove("itheima")
print(f"通过remove方法移除元素后，列表结果是{mylist}")  # 只删除了1个

# 8. 清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 9. 统计列表内某元素的数量
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = mylist.count("itheima")
print(f"列表中itheima的数量是：{count}")

# 10. 统计列表中全部的元素数量
count = len(mylist)
print(f"列表中的元素数量是：{count}个")

"""
演示tuple元组的定义与操作
元组的内容不得被修改
"""

# 定义元组
t1 = (1, "Hi", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是{t1}")
print(f"t2的类型是：{type(t2)},内容是{t2}")
print(f"t3的类型是：{type(t3)},内容是{t3}")

# 定义单个元素的元素
t4 = ("hello",)  # 定义单个元素要加逗号
print(f"t4的类型是：{type(t4)},内容是{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)},内容是{t5}")
num = t5[1][2]
print(f"从元组当中取出的数据是{num}")

# 元组的操作：index查找方法
t6 = ("传智教育", "黑马程序员", "666")
index = t6.index("666")
print(f"在元组t6中，查找666的下标是：{index}")

# 元组的操作：count统计方法
t7 = ("传智教育", "黑马程序员", "666", "666", "666", "666")
num = t7.count("666")
print(f"在元组t7中，666的数量有{num}个")

# 元组的操作：len函数统计元组元素数量
t8 = ("传智教育", "黑马程序员", "666", "666", "666", "666")
length = len(t8)
print(f"t8元组中有{length}个元素")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1

# 元组的遍历：for
for element in t8:
    print(f"元组的元素有：{element}")

# 定义一个元组
t9 = (1, 2, ["666", "abc"])
print(f"t9的内容是：{t9}")
t9[2][0] = "qwer"
t9[2][1] = "uiop"
print(f"t9的内容是：{t9}")  # 元组内容没变，列表内容改变

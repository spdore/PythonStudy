my_list = [21, 25, 21, 23, 22, 20]
print(my_list)
my_list.append(31)
print(my_list)
my_list.extend([29, 33, 30])
print(my_list)
num1 = my_list[0]
print(f"从列表中取出的第一个元素应该是21，实际上是{num1}")
num2 = my_list[-1]
print(f"从列表中取出最后一个元素应该是30，实际上是{num2}")
index = my_list.index(31)
print(f"元素31在列表的下标位置是：{index}")
print(my_list)
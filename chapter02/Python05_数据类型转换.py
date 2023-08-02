# 将数字类型转换为字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

# 将字符串转换为数字
num = int("666")
print(type(num), num)

num_1 = float("3.14")
print(type(num_1), num_1)

# 错误示例，想要将字符串转化为数字，必须要求字符串内的内容全是数字
'''
num_2 = int("okays")
print(type(num_3), num_3)
'''

# 整数转浮点数
num_3 = float(5)
print(type(num_3), num_3)

# 浮点数转整数
num_4 = int(5.6)
print(type(num_4), num_4)  # 向下取整

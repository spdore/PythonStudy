"""
Python中的各类运算符
"""

# 算术运算符
print("1 + 1 = ", 1 + 1)
print("1 - 1 = ", 1 - 1)
print("2 * 3 = ", 2 * 3)
print("6 / 2 = ", 6 / 2)
print("9 // 2 = ", 9 // 2)  # 取整除
print("9 % 2 = ", 9 % 2)  # 取余
print("9 ** 2 = ", 9 ** 2)  # 乘方

# 赋值运算符
num = 1 + 2 * 3
# 复合赋值运算符
# +=
num = 1
num += 1 # num = num + 1
print("num += 1: ", num)
num -= 1
print("num -= 1: ", num)
num *= 4
print("num *= 4: ", num)
num /= 2
print("num /= 2: ", num)

num = 3
num %= 2
print("num %= 2: ", num)

num = 3
num **= 2
print("num **= 2: ", num)

num //= 2
print("num //= 2: ", num)
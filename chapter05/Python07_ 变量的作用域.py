"""
演示函数使用时，定义的变量作用域
"""


# 演示局部变量
def test_a():
    num = 100
    print(num)


test_a()
# 出了函数体，局部变量无法使用
# print(num)

# 演示全局变量
num = 200


def test_b():
    print(f"test_b_num:{num}")


def test_c():
    print(f"test_c_num:{num}")


test_b()
test_c()
print(num)

# 在函数内修改全局变量
num = 200


def test_d():
    print(f"test_d_num:{num}")


def test_e():
    num = 500  # 此时num为局部变量，在函数内部正常使用
    print(f"test_e_num:{num}")


def test_f():
    global num
    num = 600  # 此时num为全局变量，全局生效
    print(f"test_f_num:{num}")


test_d()
test_e()
test_f()
print(num)

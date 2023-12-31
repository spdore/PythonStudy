"""
演示lambda匿名函数
"""


# 定义一个函数，接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果是：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test_func(lambda x, y: x + y)

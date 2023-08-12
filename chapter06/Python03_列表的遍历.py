"""
演示对列表的循环，使用while和for两种循环方式
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = [1, 2, 3, 4]
    # 循环控制变量通过下标索引来控制，默认0
    # 每次循环都将下标索引变量+1
    # 循环条件：下标索引变量 < 列表元素数量

    # 定义一个变量标记列表下标
    index = 0

    while index < len(my_list):
        element = my_list[index]
        print(f"列表元素的值为:{element}")
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:None
    """
    my_list = [1, 2, 3, 4, 5]
    # for 临时变量 in 数据容器
    for element in my_list:
        print(f"列表元素的值为:{element}")


list_while_func()
list_for_func()

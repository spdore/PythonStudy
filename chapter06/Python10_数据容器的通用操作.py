"""
演示数据容器的通用功能
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"Key1": 1, "Key2": 2, "Key3": 3, "Key4": 4, "Key5": 5}

# len元素个数
print(f"列表\t\t元素个数有：{len(my_list)}")
print(f"元组\t\t元素个数有：{len(my_tuple)}")
print(f"字符串\t元素个数有：{len(my_str)}")
print(f"集合\t\t元素个数有：{len(my_set)}")
print(f"字典\t\t元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表\t\t最大的元素是：{max(my_list)}")
print(f"元组\t\t最大的元素是：{max(my_tuple)}")
print(f"字符串\t最大的元素是：{max(my_str)}")
print(f"集合\t\t最大的元素是：{max(my_set)}")
print(f"字典\t\t最大的元素是：{max(my_dict)}")  # 统计的Key的大小

# min最小元素
print(f"列表\t\t最小的元素是：{min(my_list)}")
print(f"元组\t\t最小的元素是：{min(my_tuple)}")
print(f"字符串\t最小的元素是：{min(my_str)}")
print(f"集合\t\t最小的元素是：{min(my_set)}")
print(f"字典\t\t最小的元素是：{min(my_dict)}")

# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")  # 抛弃Value只留Key

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")  # 抛弃Value只留Key

# 类型转换：容器转字符串  变成字符串了
print(f"列表转字符串的结果是：{str(my_list)}")  # "[1, 2, 3, 4, 5]"
print(f"元组字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")  # 抛弃Value只留Key

# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")  # 数据无序且无重复
print(f"字典转集合的结果是：{set(my_dict)}")  # 抛弃Value只留Key

# 进行容器的排序
my_list = [1, 3, 2, 5, 4]
my_tuple = (1, 3, 2, 4, 5)
my_str = "abcfedg"
my_set = {1, 2, 5, 4, 3}
my_dict = {"Key1": 1, "Key2": 2, "Key3": 3, "Key4": 4, "Key5": 5}

# 排序完成全部变成列表
print(f"列表排序的结果是：{sorted(my_list)}")
print(f"元组排序的结果是：{sorted(my_tuple)}")
print(f"字符串排序的结果是：{sorted(my_str)}")
print(f"集合排序的结果是：{sorted(my_set)}")
print(f"字典排序的结果是：{sorted(my_dict)}")  # 只排序Key

print(f"列表反向排序的结果是：{sorted(my_list,reverse=True)}")
print(f"元组反向排序的结果是：{sorted(my_tuple,reverse=True)}")
print(f"字符串反向排序的结果是：{sorted(my_str,reverse=True)}")
print(f"集合反向排序的结果是：{sorted(my_set,reverse=True)}")
print(f"字典反向排序的结果是：{sorted(my_dict,reverse=True)}")

# 类型转换：容器转列表

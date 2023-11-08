"""
演示对文件的读取
"""
import time

# 打开文件
# f = open("E:\测试文件\spec.txt", "r", encoding="UTF-8")
# print(type(f))

# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")  # 下一次read是接着上一次read进行的
# print("------------------------------------------")

# 读取文件 - readLines()
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的类内容：{lines}")  # 每一行的内容作为一个列表元素

# 读取文件 - readline()  一次读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# 文件关闭
# f.close()
# time.sleep(100000)

# with open 语法操作文件
with open("E:\测试文件\spec.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")  # 执行完毕后自动关闭文件

time.sleep(100000)

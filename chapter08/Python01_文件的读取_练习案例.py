"""
演示读取文件课后练习题
"""

# 打开文件，以读取模式打开
f = open("E:/测试文件/python8_1.txt", "r", encoding="UTF-8")

# 读取文件全部内容统计信息
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中出现了{count}次")

# 一行行读取
count = 0  # 计数器
for line in f:
    line = line.strip()  # 取出开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1  # 计数器加1

print(f"itheima出现次数为{count}次")
# 关闭文件
f.close()

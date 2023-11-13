"""
演示对文件的写入
"""

import time

# # 打开一个不存在的文件
# f = open("E:/测试文件/test.txt", "w", encoding="UTF-8")
#
# # write写入
# f.write("Hello World!")  # 内容写入内存当中
#
# # flush刷新
# f.flush()  # 将内存中积攒的内容写入硬盘
#
# # close关闭
# f.close()  # close方法内置了flush功能

# 打开一个存在的文件
f = open("E:/测试文件/test.txt", "w", encoding="UTF-8")  # w模式如果文件之前不存在会先创建文件再写入，如果文件之前存在则会清空文件再写入

# write写入
f.write("666")  # 内容写入内存当中

# flush刷新
f.flush()  # 将内存中积攒的内容写入硬盘
f.close()
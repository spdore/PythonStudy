"""
文件操作综合案例
"""

# 打开文件得到文件对象，准备读取
fr = open("E:/测试文件/bill.txt", "r", encoding="UTF-8")
# 打开文件得到文件对象，准备写入
fw = open("E:/测试文件/bill.txt.bak", "w", encoding="UTF-8")
# for循环读取文件
for line in fr:
    line = line.strip()
    # 判断内容，写入满足条件的内容
    if line.split(" ")[1] == "测试":
        continue
    fw.write(line)
    # 由于之前对数据进行了strip操作，需要写回换行符
    fw.write("\n")

# close2个文件对象
fr.close()
fw.close()

"""
演示while循环打印9 * 9乘法表
"""
i = 1
j = 1
while i < 10:
    while j <= i:
        print(f"{i} * {j} = {i * j}\t", end='')
        j += 1
    print("")
    i += 1
    j = 1

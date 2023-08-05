"""
演示while循环的嵌套使用
"""
day = 1
while day <= 100:
    print(f"今天是第{day}天，准备表白")
    i = 1
    while i <= 10:
        print(f"我送小美{i}朵花")
        i += 1
    day += 1
    print("小美我喜欢你")
print(f"坚持到第{day - 1}天，表白失败了")
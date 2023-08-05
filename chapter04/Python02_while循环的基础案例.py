"""
演示while循环的基础案例 —— 猜数字
"""
import random
num = random.randint(1, 10)
i = 1
flag = True
while flag:
    guess = int(input("请输入你猜的数字："))
    if guess == num:
        print(f"恭喜你，第{i}次就猜中了")
        flag = False
    else:
        i += 1
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")

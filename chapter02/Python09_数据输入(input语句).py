"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁？")
name = input()
print(f"我知道了，你是{name}")

num = input("告诉我你有多少钱！")  # 默认接收类型为字符串
num = int(num)
print(f"你才{num}块钱，真穷！", type(num))

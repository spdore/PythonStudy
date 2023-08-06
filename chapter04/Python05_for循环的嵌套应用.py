"""
演示嵌套应用for循环
"""

i = 0
# 坚持表白一百天，每天送十朵花
for i in range(100):
    print(f"今天是表白的第{i + 1}天。")
    for j in range(10):
        print(f"这是我送给小美的第{j + 1}朵花")
print(f"第{i}天，表白成功了")
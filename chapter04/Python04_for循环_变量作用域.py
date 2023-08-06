"""
演示Python for循环临时变量的作用域
"""

i = 0
for i in range(5):  # 作用域限定为for循环之内，但外部也可以访问，如需访问该临时变量可以实现在循环外定义它
    print(i)
print(i)

"""
演示循环语句的中断控制:break和continue
"""
# 演示循环中断语句 continue
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")  #此时continue语句不起作用
print("")

# 演示continue语句的嵌套使用
for i in range(1, 6):
    print("语句一")
    for j in range(1, 6):
        print("语句二")
        continue
        print("语句三")  #此时continue语句跳过语句三，中断当前循环进入下一次
    print("语句四")
print("")

# 演示循环中断语句 break
for i in range(1, 101):
    print("yuju1")
    break  # break掉之后直接结束所在循环
    print("yuju2")
print("yuju3")
print("")

# 演示break语句的嵌套使用
for i in range(1, 6):
    print("语句一")
    for j in range(1, 6):
        print("语句二")
        break
        print("语句三")
    print("语句四")
num_real = 10

if int(input("请输入第一次猜想的数字：")) == num_real:
    print("恭喜你，第一次就猜对了！")
elif int(input("猜错了，再猜一次：")) == num_real:
    print("猜对了！")
elif int(input("猜错了，再猜一次：")) == num_real:
    print("最后一次机会，你猜对了！")
else:
    print("Sorry，你猜错了")

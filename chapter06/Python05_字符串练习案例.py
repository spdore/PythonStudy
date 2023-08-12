s1 = "itheima itcast boxuegu"
count = s1.count("it")
print(f"字符串{s1}中有：{count}个it字符")
s2 = s1.replace(" ","|")
print(f"字符串{s1}，被替换空格后，结果是{s2}")
s2_list = s2.split("|")
print(f"字符串{s2}按照|分割后，得到{s2_list}")

# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)

# 通过占位的形式完成数字与字符串的拼接
# %s字符串 %d整型 %d浮点型
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)

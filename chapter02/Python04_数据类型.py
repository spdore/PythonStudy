# 方法1： 使用print直接输出类型信息
print(type("666"))
print(type(666))
print(type(66.6))

# 方法2： 使用变量存储type()语句的结果
string_type = type("666")
int_type = type(666)
float_type = type(66.6)
print(string_type)
print(int_type)
print(float_type)

# 方法3：使用type()语句，查看变量中存储的数据类型信息
name = "黑马程序员"
name_type = type(name)
print(name_type)

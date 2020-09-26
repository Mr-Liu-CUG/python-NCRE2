# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

data = input()  # 姓名 年龄 性别
av , count, n = 0, 0, 0
while data:
    n += 1
    data = data.strip().split()
    if data[1] == '男':
        count += 1
    av += eval(data[2])
    data = input()
av = av / n
print("平均年龄是{:.2f} 男性人数是{}".format(av,count))

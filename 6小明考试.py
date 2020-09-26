# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


data = input()  # 课程名 考分
s, l, av = {}, [], 0
while data:
    data = data.strip().split()
    s[data[0]] = eval(data[1])
    l.append(eval(data[1]))
    data = input()
ls = list(s.items())
ls.sort(key=lambda x: x[1], reverse=True)
av = sum(l)/len(s)
print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(ls[0][0], ls[0][1],
                                                  ls[-1][0], ls[-1][1], av))

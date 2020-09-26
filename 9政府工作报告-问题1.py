import jieba

f = open("政府工作报告2019.txt", "r", encoding="utf-8")
txt = f.read()
f.close()

words = jieba.lcut(txt)
d = {}
print("2019:", end="")
for word in words:
    if len(word) >= 2:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    if i < 9:

        print("{}:{}".format(ls[i][0], ls[i][1]), end=",")
    else:
        print("{}:{}".format(ls[i][0], ls[i][1]))

f = open("政府工作报告2018.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
print("2018:", end="")
words = jieba.lcut(txt)
d = {}
for word in words:
    if len(word) >= 2:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    if i < 9:

        print("{}:{}".format(ls[i][0], ls[i][1]), end=",")
    else:
        print("{}:{}".format(ls[i][0], ls[i][1]))

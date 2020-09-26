import jieba
f = open("data.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
words = jieba.lcut(txt)
d = {}
L = []
f = open("out2.txt", "w", encoding="utf-8")
for word in words:
    if len(word) >= 3:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True)
"""
for i in range(len(ls)):
    if i < len(ls) - 1:
        f.write("{}:{}".format(ls[i][0], ls[i][1]))
        f.write("\n")
    else:
        f.write("{}:{}".format(ls[i][0], ls[i][1]))
"""
#以下写法不正确，末尾会产生空行。上面末尾没有空行的写法才对
for i in range(len(ls)):
    f.write("{}:{}".format(ls[i][0], ls[i][1]))
    f.write("\n")
f.close()

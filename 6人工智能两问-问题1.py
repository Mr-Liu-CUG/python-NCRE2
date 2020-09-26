import jieba
f = open("data.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
words = jieba.lcut(txt)
d = {}
L = []
f = open("out1.txt", "w", encoding="utf-8")
for word in words:
    if len(word) >= 3:
        d[word] = d.get(word, 0) + 1
for key in d:
    L.append(key)
f.write("\n".join(L))
f.close()

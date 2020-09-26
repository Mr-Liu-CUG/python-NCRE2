import jieba

f = open("政府工作报告2019.txt", "r", encoding="utf-8")
txt = f.read()
f.close()

words = jieba.lcut(txt)
d = {}

L1 = []
for word in words:
    if len(word) >= 2:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    L1.append(ls[i][0])

f = open("政府工作报告2018.txt", "r", encoding="utf-8")
txt = f.read()
f.close()

words = jieba.lcut(txt)
d = {}

L2 = []
for word in words:
    if len(word) >= 2:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    L2.append(ls[i][0])

L3 = []  # 共有
L4 = []  # 2019
L5 = []  # 2018
for i in range(10):
    if L1[i] in L2:
        L3.append(L1[i])
for i in range(10):
    if L1[i] not in L2:
        L4.append(L1[i])
for i in range(10):
    if L2[i] not in L1:
        L5.append(L2[i])
print("共有词语:", end="")
# for i in range(len(L3)):
print(",".join(L3))
print("2019特有:", end="")
# for i in range(len(L4)):
print(",".join(L4))
print("2018特有:", end="")
# for i in range(len(L5)):
print(",".join(L5))

f = open("score.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("candidate0.txt", "w", encoding="utf-8")
D = []  # 所有学生信息
L = []  # 单个学生信息
for line in lines:
    L = line.strip().split()
    s = 0
    for j in range(2, 12):
        s += eval(L[j])
    L.append(s)
    D.append(L)
D.sort(key=lambda x: x[-1], reverse=True)
for i in range(10):
    f.write(" ".join(D[i][-1])+'\n')
f.close()

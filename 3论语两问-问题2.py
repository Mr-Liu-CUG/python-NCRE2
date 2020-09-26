f = open("论语-原文.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("论语-提纯原文.txt", "w", encoding="utf-8")
for line in lines:
    for i in range(100):
        j = "(" + str(i) + ")"
        if j in line:
            line = line.replace(j, "")
    f.write(line)

f.close()

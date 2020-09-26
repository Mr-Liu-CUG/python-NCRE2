f = open("candidate0.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("candidate.txt", "w", encoding="utf-8")
for line in lines:
    flag = 0
    line = line.strip().split()
    for i in range(2, 12):
        if eval(line[i]) >= 60:
            flag += 1
    if flag == 10:
        f.write("{}{}\n".format(line[0], line[1]))  # 该处姓名与学号之间没有空格
f.close()

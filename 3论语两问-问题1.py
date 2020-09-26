f = open("论语.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("论语-原文.txt", "w", encoding="utf-8")
flag = 1
for line in lines:
    if "原文" in line:
        flag = 1
    if "注释" in line:
        flag = 0
    if flag == 1 and "原文" not in line:
        line = line.strip(" ")
        if line != '\n':  # 排除空行
            f.write(line)
f.close()

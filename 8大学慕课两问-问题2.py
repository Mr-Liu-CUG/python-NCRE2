f = open("univ.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
m, n = 0, 0
for line in lines:
    line = line.strip()
    if "大学生" in line:
        continue

    elif "大学" in line and "学院" in line:
        if line[-2:] == "大学":
            print(line)
            m += 1  # 统计大学数目
        if line[-2:] == "学院":
            print(line)
            n += 1  # 统计大学数目
    elif "大学" in line:
        print(line)
        m += 1  # 统计大学数目
    elif "学院" in line:
        print(line)
        n += 1  # 统计学院数目
print("包含大学的名称数量是{}".format(m))
print("包含学院的名称数量是{}".format(n))

f = open("PY301-SunSign.csv", "r")
lines = f.readlines()
f.close()
s = input("请输入星座序号（例如，5）：").split()
while s:
    for i in s:
        for line in lines:
            line = line.strip().split(",")
            if line[0] == i:
                print("{}({})的生日是{}月{}日至{}月{}日之间".format(line[1], line[4],
                                                     line[2][:-2], line[2][-2:],
                                                     line[3][:-2], line[3][-2:]))
    s = input("请输入星座序号（例如，5）：").split()
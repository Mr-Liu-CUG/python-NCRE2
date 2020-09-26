f = open("PY301-SunSign.csv", "r")
lines = f.readlines()
f.close()
s = input("请输入星座中文名称（例如，双子座）：")
for line in lines:
    line = line.strip().split(",")
    if line[1] == s:
        print("{}的生日位于{}-{}之间".format(line[1],line[2], line[3]))
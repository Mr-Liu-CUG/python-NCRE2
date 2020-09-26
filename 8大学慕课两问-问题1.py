f = open("data.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("univ.txt", "w", encoding="utf-8")
for line in lines:
    if "alt=" in line:
        line = line.strip().split("alt=")[1].split('\"')[1]
        f.write(line + "\n")
f.close()

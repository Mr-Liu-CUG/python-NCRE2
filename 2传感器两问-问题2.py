f = open("earpa001.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("earpa001_count.txt", "w", encoding="utf-8")
d = {}
for line in lines:
    line = line.strip().split(",")
    d[line[-1]] = d.get(line[-1], 0) + 1
for key in d:
    f.write("1-" + key + "," + str(d[key]) + "\n")

f.close()
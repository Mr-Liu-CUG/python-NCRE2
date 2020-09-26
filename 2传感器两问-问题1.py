f = open("sensor.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
fo = open("earpa001.txt", "w", encoding="utf-8")
for line in lines:
    line = line.strip().split(",")
    if line[1] == " earpa001":
        fo.write('{},{},{},{}\n'.format(line[0], line[1], line[2], line[3]))
fo.close()

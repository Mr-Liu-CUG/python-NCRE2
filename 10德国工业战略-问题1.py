f = open("data.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
f = open("clean.txt", "w", encoding="utf-8")
st = "（），。？‘’“”！  、\n"
for i in txt:
    if i in st:
        txt = txt.replace(i, "")
f.write(txt)
f.close()

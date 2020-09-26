f = open("命运.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
d = {}
#sym = "，。、？：‘’”“！"
#for i in sym:
#    if i in txt:
#        txt = txt.replace(i, '')
txt = txt.replace("\n", "")
for i in txt:
    d[i] = d.get(i, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    print("{}".format(ls[i][0]),end="")
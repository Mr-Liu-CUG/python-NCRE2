f = open("命运.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
d = {}
#sym = "，。、？：‘’”“！"
#for i in sym:
#    if i in txt:
#        txt = txt.replace(i, '')
txt = txt.replace("\n", "").replace(" ", "")
for i in txt:
    d[i] = d.get(i, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True)
f = open("命运-频次排序.txt", "w", encoding="utf-8")
for i in range(len(ls) - 1):
    f.write(ls[i][0] + ":" + str(ls[i][1]) + ",")
f.write(ls[-1][0] + ":" + str(ls[-1][1]))
f.close()

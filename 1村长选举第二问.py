f=open("name.txt", 'r', encoding='utf-8')
names=f.readlines()
f.close()
f=open("vote.txt", 'r', encoding='utf-8')
votes=f.readlines()
f.close()
D={}
NUM=0
for vote in votes:
    num = len(vote.split())
    if num==1 and vote in names:
        D[vote[:-1]]=D.get(vote[:-1], 0)+1
        NUM+=1
l=list(D.items())
l.sort(key=lambda s:s[1], reverse=True)
name=l[0][0]
score=l[0][1]
print("有效票数为：{} 当选村民为:{}，票数为：{}".format(NUM, name, score))


f=open("vote.txt", "r", encoding="utf-8")
votes=f.readlines()
f.close()
f=open("name.txt", "r", encoding="utf-8")
names=f.readlines()
f.close()
D={}
NUM=0
for vote in votes:
    num = len(vote.split())
    if num==1 and vote in names:
        D[vote[:-1]]=D.get(vote[:-1], 0)+1
        NUM+=1
    else:
        with open("vote1.txt","a+",encoding="utf-8") as fi:
            fi.write("{}".format(vote))
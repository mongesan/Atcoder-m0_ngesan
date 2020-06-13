X,Y=map(int, input().split())
l=[0,300000,200000,100000]
for i in range(202):
    l.append(0)
sc=l[X]+l[Y]
print(sc+400000 if X==Y==1 else sc)
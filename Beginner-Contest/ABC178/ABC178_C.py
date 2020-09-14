nt=[]
x=[]
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        nt=[str(i),str(j),str(k),str(l),str(m),str(n)]
                        if nt.count('0')>=1 and nt.count('9')>=1:
                            x.append(''.join(nt))
x=list(set(x))
print(sorted(x))
print(len(x))

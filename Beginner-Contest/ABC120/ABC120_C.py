from collections import Counter
S = input()
l = list()
for i in S:
    l.append(i)
c = Counter(l)
print(min(c['0'], c['1'])*2)

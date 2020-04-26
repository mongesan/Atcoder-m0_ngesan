import collections
n = int(input())
l = list()
for i in range(n):
    l.append(str(input()))
c = collections.Counter(l)
print(len(c))

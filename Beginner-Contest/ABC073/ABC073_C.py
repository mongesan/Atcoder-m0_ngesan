from collections import Counter
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

c = Counter(l)
cnt = len(c)
l = list(c.most_common(len(c)))
for t in l:
    i = t[1]
    if i % 2 == 0:
        cnt -= 1
print(cnt)

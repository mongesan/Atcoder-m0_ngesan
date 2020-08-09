n = int(input())
l = []
for i in range(n):
    s = str(input())
    l.append((s[::-1], s))

l.sort()
for k, v in l:
    print(v)

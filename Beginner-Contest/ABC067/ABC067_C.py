n = int(input())
a = list(map(int, input().split()))
l = []
x = 0
s = sum(a)
for i in range(n-1):
    x+=a[i]
    l.append(abs(x*2-s))
print(min(l))
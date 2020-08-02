from collections import Counter
from math import factorial


def combinations_count(n, r):
    if n < 2:
        return 0
    else:
        return factorial(n)//(factorial(n-r)*factorial(r))


n = int(input())
A = list(map(int, input().split()))
m = 0
c = Counter(A)
d = Counter([])
for k, v in c.items():
    co = combinations_count(v, 2)
    d[k] = co
    m += co
# print(c)
# print(d)
if c[A[0]]==n:
    x=combinations_count(n-1, 2)
for a in A:
    if c[a]==n:
        print(x)
    elif c[a]<=2:
        print(m-d[a])
    else:
        print(m-d[a]+1)

from math import factorial
from collections import Counter


def combinations_count(n, r):
    if n >= r:
        return factorial(n) // (factorial(n - r) * factorial(r))
    else:
        return 0

c = Counter()
n = int(input())
A = list(map(int, input().split()))
for i in A:
    c[i] += 1
ans = 0
for k, v in c.items():
    ans += combinations_count(v, 2)

for i in A:
    print(ans-c[i]+1)

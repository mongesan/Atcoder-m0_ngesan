import collections
import math
# math.gcd(a,b)
k = int(input())
cnts = collections.defaultdict(int)
for i in range(1, k+1):
    for j in range(1, k+1):
        cnts[math.gcd(i,j)] += 1
ans = 0
for i in range(1, k+1):
    for key in cnts.keys():
        ans += math.gcd(i, key)*cnts[key]
print(ans)

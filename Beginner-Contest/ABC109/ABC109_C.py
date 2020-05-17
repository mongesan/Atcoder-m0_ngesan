import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)


N, X = map(int, input().split())
x = list(map(int, input().split()))
y = []
for i in range(N-1):
    y.append(x[i+1]-x[i])

print(if gcd_list(y))

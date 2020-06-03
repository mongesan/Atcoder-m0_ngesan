from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

N, X=map(int, input().split())
x=list(map(int, input().split()))
y=list()

for i in x:
    y.append(abs(X-i))

#print(y)
print(gcd_list(y))
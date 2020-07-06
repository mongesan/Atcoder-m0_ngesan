from math import gcd
from functools import reduce
def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

print(lcm_list(l))
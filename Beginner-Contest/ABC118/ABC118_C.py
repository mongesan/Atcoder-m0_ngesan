from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

N=int(input())
a=list(map(int, input().split()))
print(gcd_list(a))
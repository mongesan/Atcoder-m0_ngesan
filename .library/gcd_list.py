from math import gcd
#if you use python3.4.3, please use
#from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

#--example--
#l = list(map(int, input().split()))
#print(gcd_list(l))
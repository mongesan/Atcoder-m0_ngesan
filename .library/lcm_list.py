from math import gcd
from functools import reduce
def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
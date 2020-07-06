from math import gcd
from functools import reduce
def gcd_list(numbers):
    return reduce(gcd, numbers)

from itertools import product
n = int(input())
d = ['a', 'b', 'c']
for s in list(product(d, repeat=n)):
    print(''.join(s))

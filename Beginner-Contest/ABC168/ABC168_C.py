from math import cos
from math import sqrt
from math import radians
A, B, H, M = map(int, input().split())
a = H*30+(M/60)*30
b = M*6
c = min(abs(a-b), abs(b-a))
if a == 0:
    a += 360
if b == 0:
    b += 360
c = min(c, abs(a-b), abs(b-a))
print(sqrt(A**2+B**2-2*A*B*cos(radians(c))))

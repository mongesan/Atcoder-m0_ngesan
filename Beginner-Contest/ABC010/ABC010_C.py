from math import sqrt


def distance(a, b, c, d):
    return(sqrt((c-a)**2+(d-b)**2))


Xa, Ya, Xb, Yb, T, V = map(int, input().split())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if distance(Xa, Ya, x, y)+distance(x, y, Xb, Yb) <= T*V:
        print('YES')
        exit()
print('NO')

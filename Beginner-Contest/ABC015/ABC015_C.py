n, k = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]

def DPS(deep, m):
    for t in T[deep]:
        r = m ^ t
        if deep == n-1:
            if r == 0:
                print('Found')
                exit()
        else:
            DPS(deep+1, m ^ t)

DPS(0, 0)
print('Nothing')

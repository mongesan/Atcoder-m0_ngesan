n = int(input())
X, Y, T=0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    if abs(x-X)+abs(y-Y) <= t-T and t % 2 == (x+y) % 2:
        continue
    else:
        print('No')
        quit()
    X, Y, T= x, y, T
print('Yes')

n = int(input())
tb,xb,yb = 0,0,0
for _ in range(n):
    ta,xa,ya = list(map(int, input().split()))
    tdiff = abs(ta-tb)
    mdiff = abs(xa-xb) + abs(ya-yb)
    if tdiff < mdiff or (tdiff + mdiff) & 1:
        print('No')
        exit()
    
    tb,xb,yb = ta,xa,ya

print('Yes')

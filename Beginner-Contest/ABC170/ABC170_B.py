x,y=map(int, input().split())
for t in range(x+1):
    if 2*t+4*(x-t)==y:
        print('Yes')
        exit()

print('No')
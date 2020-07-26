from sys import setrecursionlimit
setrecursionlimit(10**9)

R,C=map(int, input().split())
sy, sx=map(int, input().split())
gy, gx=map(int, input().split())
l=[[ch for ch in str(input())] for i in range(R)]
sy-=1
sx-=1
gy-=1
gx-=1
ans=2500
#print(l[gx][gy])
def BFS(y, x, history, cnt):
    if history[y][x]=='0':
        for h in history:
                print(''.join(h))
        history[y][x]='1'
        if x==gx and y==gy:
            global ans
            ans=min(ans, cnt)
        else:
            cnt+=1
            if l[y+1][x]=='.':
                print('down')
                BFS(y+1, x, history, cnt)
            
            if l[y-1][x]=='.':
                BFS(y-1, x, history, cnt)
            
            if l[y][x+1]=='.':
                print('right')
                BFS(y, x+1, history, cnt)

            if l[y][x-1]=='.':
                BFS(y, x-1, history, cnt)
BFS(sx, sy, [['0' for _ in range(C)] for _ in range(R)], 0)
print(ans)
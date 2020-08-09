R,G,B,n=map(int, input().split())
cnt=0
for r in range(n+1):
    for g in range(n+1):
        b=(n-r*R-g*G)/B
        #print(r,g,b)
        if b>=0:
            if b==int(b):
                cnt+=1

print(cnt)
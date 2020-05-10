N, K=map(int, input().split())
per=int()
for i in range(1,N+1):
    cnt=int()
    while i*(2**cnt)<K:
        cnt+=1
    #print(cnt)
    per+=(1/N)*((1/2)**cnt)

print(per)
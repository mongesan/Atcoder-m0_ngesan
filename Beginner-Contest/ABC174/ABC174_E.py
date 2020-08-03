k=int(input())
n=str(7)
for i in range(10**6):
    n+='7'
    if int(n)%k==0:
        print(i+2)
        exit()
print(-1)
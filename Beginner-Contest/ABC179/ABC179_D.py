from math import sqrt
n=int(input())
cnt=0
for i in range(1,n+1):
    cnt+=int(sqrt(i))
print(cnt)
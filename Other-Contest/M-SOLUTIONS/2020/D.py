n=int(input())
a=list(map(int, input().split()))
k=0
for i in range(n-1):
    if a[i]<a[i+1]:
        k=n%a[i]
    else:
        
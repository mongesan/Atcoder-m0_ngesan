from math import factorial
n,m=map(int, input().split())
ans=0
if abs(n-m)==0:
    ans=factorial(n)*factorial(m)*2
elif abs(n-m)==1:
    ans=factorial(n)*factorial(m)

print(ans%(10**9+7))
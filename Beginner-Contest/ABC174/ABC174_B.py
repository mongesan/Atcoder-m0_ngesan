from math import sqrt
n,d=map(int, input().split())
a=0
for i in range(n):
    x,y=map(int, input().split())
    #print(sqrt(x**2+y**2), d)
    if sqrt(x**2+y**2)<=d:
        a+=1

print(a)
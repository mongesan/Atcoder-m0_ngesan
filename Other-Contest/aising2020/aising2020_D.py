n=int(input())
x=int(input())
for i in range(n):
    print(format(x, '0'+ str(n-1) +'b'))
    
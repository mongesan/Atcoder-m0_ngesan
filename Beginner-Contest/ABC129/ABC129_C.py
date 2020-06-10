n, m=map(int, input().split())
A = list()
Fib = [1,1,1]
for i in range(m):
    A.append(int(input()))
x = 0
for i in range(3,n+1):
    Fib.append(Fib[i-1]+Fib[i-2])
print(Fib)
sp = 0
cnt = 1
for M in A:
    cnt*=Fib[M-sp]
    print(cnt)
    if M-sp == 1:
        if M!=1:
            cnt *= 0
    sp=M
cnt*=Fib[n-sp]
print(cnt % 1000000007)

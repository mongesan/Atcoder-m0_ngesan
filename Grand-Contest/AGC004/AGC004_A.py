n = int(input())
b, d = 0, '='
cnt = 0
A = list(map(int, input().split()))
tmp = []
for i in range(n):
    a = A[i]
    print(a, b, d)
    if d=='=':
        if a>b:
            ('+')
        elif a<b:
            print('-')
        else:
            print('=')
    else:
        if a == b:
            d = '='
            tmp.append(a)
        elif a > b and d != '+':
            d = '+'
            cnt += 1
            print('+',tmp)
            tmp=[]
        elif a < b and d != '-':
            d = '-'
            cnt += 1
            print('-',tmp)
            tmp=[]
        else:
            tmp.append(a)
        b = a

print(cnt)

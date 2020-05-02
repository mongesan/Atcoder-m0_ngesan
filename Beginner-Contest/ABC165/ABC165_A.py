K = int(input())
A, B = map(int, input().split())
l = list()
cnt = 1
while cnt * K <= 1000:
    l.append(cnt*K)
    cnt += 1

for i in l:
    if A <= i <= B:
        print('OK')
        exit()

print('NG')

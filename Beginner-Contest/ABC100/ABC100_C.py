n = int(input())
A = list(map(int, input().split()))
cnt = int()

for a in A:
    cnt += format(a, 'b')[::-1].find('1')

print(cnt)
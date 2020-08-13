n = int(input())
A = list(map(int, input().split()))
b = A[0]
att = ''
cnt = 1
for a in A:
    # print(a,b,att)
    if a != b:
        if att == '':
            if a > b:
                att = '+'
            elif a < b:
                att = '-'
        elif att == '+':
            if a < b:
                cnt += 1
                att = ''
        elif att == '-':
            if a > b:
                cnt += 1
                att = ''
    b = a
print(cnt)

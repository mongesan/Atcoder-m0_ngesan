S = str(input())
n = len(S)
cnt = 0
i = 1
for ch in S:
    if ch == 'U':
        cnt += (i-1)*2
        cnt += n-i
    else:
        cnt += (n-i)*2
        cnt += i-1
    i += 1

print(cnt)

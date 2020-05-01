n = int(input())
s = str(input())
t = str()
cnt = int()
for ch in s:
    if t[-1:] != ch:
        t += ch
        cnt += 1

print(cnt)

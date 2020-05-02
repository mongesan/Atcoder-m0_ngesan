X = int(input())
cnt = 100
i = 0
while cnt < X:
    cnt += int(str(cnt)[:-2])
    i += 1

print(i)

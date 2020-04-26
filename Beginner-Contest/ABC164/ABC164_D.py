s = str(input())
l = len(s)
ep = l
ep += 0 if int(s) % 2019 == 0 else 1
cnt=int()
for i in range(5, ep+1):
    for j in range(l-i+1):
        if int(s[0+j:i+j])%2019==0:
            cnt+=1

print(cnt)
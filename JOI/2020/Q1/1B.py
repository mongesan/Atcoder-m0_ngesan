n = int(input())
s = str(input())
l = ['a','i','u','e','o']
cnt=0
for ch in s:
    if ch in l:
        cnt+=1

print(cnt)
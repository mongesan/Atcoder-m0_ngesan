n = int(input())
h = list(map(int, input().split()))
ans = 0
cnt = 0

for i in range(n-1):
    if h[i] < h[i+1]:
        #print(cnt)
        ans = max(ans, cnt)
        cnt = -1
    cnt += 1

#print(cnt)
ans = max(ans, cnt)
print(ans)

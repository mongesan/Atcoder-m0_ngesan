S = str(input())
T = str(input())
n = len(S)
m = len(T)
ans = m
for i in range(n-m+1):
    x = m
    s = S[i:i+m]
    for j in range(m):
        if s[j] == T[j]:
            x -= 1
    ans = min(ans, x)

print(ans)

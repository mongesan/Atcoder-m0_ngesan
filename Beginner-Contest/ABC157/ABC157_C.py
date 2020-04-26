n, m = map(int, input().split())

ans = [-1 for i in range(n)]

pf = True
for i in range(m):
    s, c = map(int, input().split())
    if ((not ans[s-1] == -1) and (not ans[s-1] == c)) or ((not n == 1)and s == 1 and c == 0):
        print(-1)
        pf = False
        break
    else:
        ans[s-1] = c

if pf and n == 1:
    if ans[0] == -1:
        print(0)
    else:
        print(ans[0])
elif pf:
    if ans[0] == -1:
        ans[0] = 1
    for i in range(n):
        if ans[i] == -1:
            ans[i] = 0
    print(''.join(map(str, ans)))

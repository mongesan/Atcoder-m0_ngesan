n, m = map(int, input().split())
route = [[] for _ in range(n)]
check = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    route[a-1].append(b-1)
pos = [0]
for i in range(2):
    # print(pos)
    tmp = list()
    for p in pos:
        for r in route[p]:
            if r == n-1:
                print('POSSIBLE')
                exit()
            if check[r-1] == 0:
                tmp.append(r)
                check[r-1] == 1
    pos = tmp

print('IMPOSSIBLE')

from itertools import combinations
n = int(input())
l = list(map(int, input().split()))
cnt = 0
for t in combinations(l, 3):
    if len(set(t))==3:
        m = max(t)
        if m < sum(t)-m:
            cnt += 1
            #print(t)
print(cnt)

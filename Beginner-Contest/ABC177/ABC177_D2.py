from collections import Counter
n, m = map(int, input().split())
koseki = [-1 for _ in range(n)]  # -1
group = []
mouyatta = Counter()
for i in range(m):
    a, b = map(int, input().split())
    #if mouyatta[tuple(sorted([a,b]))]==0:
        #mouyatta[tuple(sorted([a,b]))]+=1
        if koseki[a-1] != -1:
            koseki[b-1] = koseki[a-1]
            group[a-1] += 1
        elif koseki[b-1] != -1:
            koseki[a-1] = koseki[b-1]
            group[b-1] += 1
        else:
            group.append(2)
            koseki[a-1] = len(group)-1
            koseki[b-1] = len(group)-1
print(max(group))

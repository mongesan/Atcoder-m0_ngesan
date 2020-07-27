n = int(input())
l = [[] for i in range(n)]
for i in range(n-1):
    l[int(input())-1].append(i+1)
#print(l)


def check(i):
    if len(l[i]) == 0:
        return 1
    else:
        m = []
        for j in l[i]:
            m.append(check(j))
        return min(m)+max(m)+1


print(check(0))

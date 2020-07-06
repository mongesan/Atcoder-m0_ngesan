from collections import Counter
N = int(input())
tmp = list(input())
da = Counter(tmp)
for _ in range(N-1):
    tmp = list(input())
    tmpd = Counter(tmp)
    for k, v in da.items():
        if not tmpd[k]:
            da[k] = 0
        else:
            da[k] = min(v, tmpd[k])
ans = ""
for k, v in da.items():
    ans += str(k)*v
a = "".join(sorted(ans))
print(a)

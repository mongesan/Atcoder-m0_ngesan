from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
cnt = 0
for k, v in Counter(a).items():
    #print(k,v)
    if k > v:
        cnt += v
    else:
        cnt += (v-k)
print(cnt)

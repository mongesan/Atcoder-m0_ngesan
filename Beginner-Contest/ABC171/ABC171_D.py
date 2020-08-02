from collections import Counter
n = int(input())
a = list(map(int, input().split()))
C = Counter(a)
q = int(input())
ans = sum(a)
for i in range(q):
    b, c = map(int, input().split())
    ans += (c-b)*C[b]
    C[c] += C[b]
    C[b] = 0
    print(ans)

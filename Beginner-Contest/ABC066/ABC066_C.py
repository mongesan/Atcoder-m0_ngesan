from collections import deque
n = int(input())
A = deque(map(str, input().split()))
B = deque()
cycle = n % 2
for a in A:
    if cycle % 2 == 1:
        B.appendleft(a)
    else:
        B.append(a)
    cycle += 1
print(' '.join(B))

n = int(input())
A = list(map(int, input().split()))
B = []
i = 1
for a in A:
    B.append((a, i))
    i += 1
B.sort()
for b in B[::-1]:
    print(b[1])

n, m, k = map(int, input().split())
tmp = list(map(int, input().split()))
A = list()
i = int()
for n in tmp:
    i+=n
    A.append(i)
tmp = list(map(int, input().split()))
B = list()
i = int()
for n in tmp:
    i+=n
    B.append(i)
# kurwa

print(A,B)
from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
C = Counter([])
X, Y = [], []
m = 0
for _ in range(n):
    a = A[m]-1
    C[m] += 1
    X.append(m)
    if C[a] != 0:
        Y = X[X.index(a):]
        X = X[:X.index(a)]
        break
    m = a
# print(X,Y)
x = len(X)
y = len(Y)
if k <= x-1:
    print(X[k]+1)
else:
    k -= x
    print(Y[k-(k//y)*y]+1)

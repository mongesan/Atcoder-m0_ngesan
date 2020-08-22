from collections import deque
n, m = map(int, input().split())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
C = deque()
t = deque()
while n != 0 or m != 0:
    if n != 0 and m != 0:
        if A[0] <= B[0]:
            C.append(A[0])
            n -= 1
            A.popleft()
        else:
            C.append(B[0])
            m -= 1
            B.popleft()
    else:
        if n == 0:
            C += B
            m = 0
        else:
            C += A
            n = 0

for i in C:
    print(i)

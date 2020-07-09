n = int(input())
m = int()
for i in range(1, 10):
    m += i*45
n = m-n
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == n:
            print("%d x %d" % (i, j))

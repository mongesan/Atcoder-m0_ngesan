N = int(input())
d = sorted(list(map(int, input().split())))
# print(d)
print(d[N//2]-d[N//2-1])

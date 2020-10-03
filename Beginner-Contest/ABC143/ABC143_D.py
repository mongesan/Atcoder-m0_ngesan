n=int(input())
l=list(map(int, input().split()))
l.sort()
l.reverse()

for i in l:
    for j in l:
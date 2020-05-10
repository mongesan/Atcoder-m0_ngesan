N = int(input())
cnt = int()
A=[]
for i in range(5):
    A.append(int(input()))
A.sort()
print(-(-N//min(A))+4)

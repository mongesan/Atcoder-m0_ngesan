import math
a, b = map(int, input().split())
ans = []
for i in range(1010): #math.ceil(1009*0.1)=100
    p8 = math.floor(i * 0.08)
    p10 = math.floor(i * 0.1)
    if p8 == a and p10 == b:
        ans.append(i)

if len(ans) != 0:
    print(min(ans))
else:
    print(-1)
a, b, c, x, y = map(int, input().split())
cost = int()
tmp = min(x, y)
x -= tmp
y -= tmp
if a+b > c*2:
    cost += tmp*2*c
else:
    cost += tmp*(a+b)

if x == 0:
    cost += min(b, c*2)*y
else:
    cost += min(a, c*2)*x

print(cost)

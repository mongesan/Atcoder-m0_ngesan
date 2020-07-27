n=int(input())
X=list(map(int, input().split()))
y=round(sum(X)/n)
cost=0
for x in X:
    cost+=(x-y)**2

print(cost)
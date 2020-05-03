N, Q = map(int, input().split())
S = str(input())
L = [0]  # ruisekiwa
for i in range(1, len(S)):
    if S[i-1:i+1] == 'AC':
        L.append(L[i-1]+1)
    else:
        L.append(L[i-1])

for i in range(Q):
    l, r = map(int, input().split())
    print(L[r-1]-L[l-1])

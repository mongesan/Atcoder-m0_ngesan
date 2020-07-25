a, b, c = map(int, input().split())
n = int(input())
for i in range(0, n+1):
    for j in range(0, n-i+1):
        k = n-i-j
        if a*(2**i) < b*(2**j) < c*(2**k):
            #print(i, j, k)
            print('Yes')
            exit()
        else:
            continue
print('No')

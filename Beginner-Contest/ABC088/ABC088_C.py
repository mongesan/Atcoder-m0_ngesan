c = [list(map(int, input().split())) for i in range(3)]
x = c[0][2]-c[0][1]
y = c[0][1]-c[0][0]
for i in range(1, 3):
    if c[i][1]-c[i][0] != y:
        print('No')
        break
    if c[i][2]-c[i][1] != x:
        print('No')
        break

else:
    print('Yes')

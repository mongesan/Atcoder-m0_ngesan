n = int(input()) % 30
ch = ['1', '2', '3', '4', '5', '6']

for i in range(0, n):
    j = i % 5
    ch[j], ch[j+1] = ch[j+1], ch[j]

print(''.join(ch))

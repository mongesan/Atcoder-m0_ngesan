from collections import Counter
n = int(input())
#l = list()
ch = ['M', 'A', 'R', 'C', 'H']
c = Counter([])
c['M'] = 0
c['A'] = 0
c['R'] = 0
c['C'] = 0
c['H'] = 0
for i in range(n):
    s = str(input())
    if s[0] in ch:
        c[s[0]] += 1
        # l.append(s[0])
cnt = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            # print(i,j,k)
            cnt += c.most_common()[i][1] * \
                c.most_common()[j][1]*c.most_common()[k][1]
print(cnt)

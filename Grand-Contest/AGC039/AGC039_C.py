s = str(input())
k = int(input())
a = s[0]
b = [s[0]]
n = 0
m = 0
for i in range(1, len(s)):
    if a == s[i]:
        a = '0'
        n += 1
    else:
        a = s[i]
    b.append(a)
print(''.join(b))
if b[0] == b[len(b)-1]:
    m += 1

print(n,m)
print(n*k-m*(k-1))

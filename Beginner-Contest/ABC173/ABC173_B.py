n = int(input())
c = [0]*4
for _ in range(n):
    s = str(input())
    if s == 'AC':
        c[0] += 1
    elif s == 'WA':
        c[1] += 1
    elif s == 'TLE':
        c[2] += 1
    else:
        c[3] += 1

print('AC x '+str(c[0]))
print('WA x '+str(c[1]))
print('TLE x '+str(c[2]))
print('RE x '+str(c[3]))

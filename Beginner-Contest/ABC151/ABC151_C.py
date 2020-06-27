N, M = map(int, input().split())
ifACL = [0]*N
cWAL = [0]*N
psL = []
AC = 0
WA = 0
p = 0
s = 0
for _ in range(M):
  p, s = map(str, input().split())
  p = int(p)
  if ifACL[p-1] == 0 and s == "WA":
    cWAL[p-1] += 1
  elif ifACL[p-1] == 0 and s == "AC":
    AC += 1
    WA += cWAL[p-1]
    ifACL[p-1] = 1

print(AC, WA)

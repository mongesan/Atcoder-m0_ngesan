n, m=map(int, input().split())
AC, WA=[0]*n, [0]*n
ac, wa=0, 0
for _ in range(m):
  p, s=list(map(str, input().split()))
  p=int(p)-1
  if AC[p]==0 and s=='WA':
    WA[p]+=1
  elif AC[p]==0 and s=='AC':
    AC[p]=1
    wa+=WA[p]
    ac+=1
  
print(ac, wa)
s=str(input())
streak=0
ans=0
for ch in s:
    if ch=='R':
        streak+=1
    else:
        ans=max(ans, streak)
        streak=0
ans=max(ans, streak)
print(ans)
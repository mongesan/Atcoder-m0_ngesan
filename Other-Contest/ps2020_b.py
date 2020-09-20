h,w=map(int, input().split())
cnt=(w//2)*h
if w%2==1:
    cnt+=h//2+h%2
if h==1 or w==1:
    cnt=1
print(cnt)
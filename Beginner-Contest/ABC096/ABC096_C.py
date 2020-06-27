h,w = map(int, input().split())
S=list()
for i in range(h):
    S.append(str(input()))

for H in range(h):
    for W in range(w):
        stat=0
        #print(H,W,S[H][W])
        if S[H][W]=='.':
            continue
        if H!=0:
            if S[H][W]==S[H-1][W]:
                stat=1
        if W!=w-1:
            if S[H][W]==S[H][W+1]:
                stat=1
        if H!=h-1:
            if S[H][W]==S[H+1][W]:
                stat=1
        if W!=0:
            if S[H][W]==S[H][W-1]:
                stat=1
        if stat==0:
            print('No')
            exit()

print('Yes')
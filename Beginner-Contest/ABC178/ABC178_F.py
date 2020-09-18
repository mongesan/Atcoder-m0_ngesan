cnt=0
for i in range(10):
    for j in range(10):
        if 0<i<9 and 0<j<9:
            continue
        else:
            print(i,j)
            cnt+=1
print(cnt)
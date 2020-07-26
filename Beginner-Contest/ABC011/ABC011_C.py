n = int(input())
NGs = sorted([int(input()), int(input()), int(input())])
if n in NGs:
    print('NO')
    exit()
else:
    cnt = 0
    while n > 0:
        cnt += 1
        if n-3 in NGs:
            if n-2 in NGs:
                if n-1 in NGs:
                    print('NO')
                    exit()
                else:
                    n -= 1
            else:
                n -= 2
        else:
            n -= 3

    # print(cnt)
    if cnt <= 100:
        print('YES')
    else:
        print('NO')

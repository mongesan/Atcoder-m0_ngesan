n = int(input())
chars="-abcdefghijklmnopqrstuvwxyz"

n_rem = n
res = ""

while True:
    x = n_rem % 26
    if x == 0:
        x = 26
    res += chars[x]
    n_rem -= x
    if n_rem == 0:
        break
    n_rem //=26

print(res[::-1])
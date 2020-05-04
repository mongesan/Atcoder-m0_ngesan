from math import factorial
X = int(input())
for i in range(1, 10**5):
    if X <= (i*(i+1))//2:
        print(i)
        break

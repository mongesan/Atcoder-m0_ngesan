from math import floor
a,b,n=map(int, input().split())
def f(a,b,x):
    return(floor(a*x/b)-a*floor(x/b))

print(f(a,b,min(b-1, n)))
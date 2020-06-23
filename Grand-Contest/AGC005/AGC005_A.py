x=str(input())
for i in range(len(x)-1):
    if x[i:i+2]=='ST':
        x=x[:i]+'--'+x[i+2:]
print(x)
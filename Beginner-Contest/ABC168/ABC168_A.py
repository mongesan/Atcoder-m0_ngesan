N=str(input())
M=int(N[len(N)-1])

h=[2,4,5,7,9]
p=[0,1,6,8]
if M in h:
    print('hon')
elif M in p:
    print('pon')
else:
    print('bon')
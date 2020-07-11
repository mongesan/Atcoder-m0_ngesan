pos = list(map(int, input().split()))
print(abs(((pos[0]-pos[4])*(pos[3]-pos[5])-(pos[2]-pos[4])*(pos[1]-pos[5]))/2))

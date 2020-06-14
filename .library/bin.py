n=int(input())
print(format(n, 'b')) #2進数へ
print(format(n, 'b')[::-1].find('1')) #bit探索
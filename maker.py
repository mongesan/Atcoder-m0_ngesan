import os
counts_of_ABC = 163
counts_of_ARC = 103
counts_of_AGC = 43

os.makedirs('Beginner-Contest')
os.chdir('Beginner-Contest')
for i in range(1, counts_of_ABC+1):
    cnt = str(i).zfill(3)
    os.makedirs('ABC'+cnt)
    os.chdir('ABC'+cnt)
    with open('ABC'+cnt+'_A.py', 'w') as f:
        f.write('#ABC'+cnt+'_A')
    with open('ABC'+cnt+'_B.py', 'w') as f:
        f.write('#ABC'+cnt+'_B')
    with open('ABC'+cnt+'_C.py', 'w') as f:
        f.write('#ABC'+cnt+'_C')
    with open('ABC'+cnt+'_D.py', 'w') as f:
        f.write('#ABC'+cnt+'_D')
    if i >= 125:
        with open('ABC'+cnt+'_E.py', 'w') as f:
            f.write('#ABC'+cnt+'_E')
        with open('ABC'+cnt+'_F.py', 'w') as f:
            f.write('#ABC'+cnt+'_F')
    os.chdir('..')
os.chdir('..')
print('ABC-file creation completed')

os.makedirs('Regular-Contest')
os.chdir('Regular-Contest')
for i in range(1, counts_of_ARC+1):
    cnt = str(i).zfill(3)
    os.makedirs('ARC'+cnt)
    os.chdir('ARC'+cnt)
    with open('ARC'+cnt+'_A.py', 'w') as f:
        f.write('#ARC'+cnt+'_A')
    with open('ARC'+cnt+'_B.py', 'w') as f:
        f.write('#ARC'+cnt+'_B')
    with open('ARC'+cnt+'_C.py', 'w') as f:
        f.write('#ARC'+cnt+'_C')
    with open('ARC'+cnt+'_D.py', 'w') as f:
        f.write('#ARC'+cnt+'_D')
    os.chdir('..')
os.chdir('..')
print('ARC-file creation completed')

os.makedirs('Grand-Contest')
os.chdir('Grand-Contest')
for i in range(1, counts_of_AGC+1):
    cnt = str(i).zfill(3)
    os.makedirs('AGC'+cnt)
    os.chdir('AGC'+cnt)
    with open('AGC'+cnt+'_A.py', 'w') as f:
        f.write('#AGC'+cnt+'_A')
    with open('AGC'+cnt+'_B.py', 'w') as f:
        f.write('#AGC'+cnt+'_B')
    with open('AGC'+cnt+'_C.py', 'w') as f:
        f.write('#AGC'+cnt+'_C')
    with open('AGC'+cnt+'_D.py', 'w') as f:
        f.write('#AGC'+cnt+'_D')
    os.chdir('..')
os.chdir('..')
print('AGC-file creation completed')

print('Completed!')
print('Good luck')

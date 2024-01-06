
while True:
    star = 11
    gap = 0
    
    for i in range(6):
        print('*', ' '*gap, '*'*star, ' '*gap, '*', sep='')
        gap += 1
        star -= 2
    for i in range(5):
        print('*', ' '*11, '*', sep='')
    print('*'*13, sep='')
    break

print('\n\n')

while True:
    star = 1
    gap = 5
    print('*'*13, sep='')
    
    for i in range(6):
        print('*', ' '*11, '*', sep='')

    for i in range(6):
        print('*', ' '*gap, '*'*star, ' '*gap, '*', sep='')
        gap -= 1
        star += 2
    break

print('\n\n')

while True:
    star = 11
    gap = 0
    for i in range(6):
        print('*', ' '*gap, '*'*star, ' '*gap, '*', sep='')
        gap += 1
        star -= 2
    star = 1
    gap = 5
    for i in range(6):
        print('*', ' '*gap, '*'*star, ' '*gap, '*', sep='')
        gap -= 1
        star += 2
    break
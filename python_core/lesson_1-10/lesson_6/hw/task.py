# в г д готово
n = 7

print('_' * 15)

for i in range(n, 0, -2):
    print('|', end='')
    for j in range((n - i) // 2):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    for j in range((n - i) // 2):
        print(' ', end=' ')
    print('|')

for i in range(1, n + 1, 2):
    print('|', end='')
    
    for j in range((n - i) // 2):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    for j in range((n - i) // 2):
        print(' ', end=' ')
    print('|')
    
print('-' * 15)


# и

n = 6
print('_' * 15)

for i in range(n, 0, -1):
    print('|', end=' ')
    for j in range(n):
        if i > j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('|')

print('_' * 15)


# К

n = 6

print('_' * 15)

for i in range(n, 0, -1):
    print('|', end=' ')
    for j in range(n):
        if (i-1) > j:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print('|')

print('-' * 15)

# A

n = 6

print('_' * 15)

for i in range(n, 0, -1):
    print('|', end=' ')
    for j in range(n):
        if i > j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('|')

print('-' * 15)


n = 6

print('_' * 15)

for i in range(n, 0, -1):
    print('|', end='')
    for j in range(n - i):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    print('|')

print('-' * 15)

n = 6

print('_' * 16)

for i in range(n, 0, -1):
    print('|', end='')
    for j in range(n - i + 1 ):
        print('*', end=' ')
    for k in range(i):
        print(' ', end=' ')
    print('|')
else:
    print('|', '* '*7, '|', sep='')

print('-' * 16)

n = 5

for i in range(1, n + 1):
    print('|', end='')
    for j in range(i):
        print('*', end='')
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('|')
    
for i in range(n - 1, 0, -1):
    print('|', end='')
    for j in range(i):
        print('*', end='')
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('|')

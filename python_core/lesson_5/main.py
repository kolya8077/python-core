# i = 0

# while i < 10:
#     i += 1
#     print(i, end=' ')

# i = 10

# while 0 < i:
#     i -= 1
#     print(i, end=' ')
    

# print('\n')
# i = 0

# while i < 10:
#     i += 1
#     print(i, end=' ')




# while 0 < i:
#     i -= 1
#     print(i, end=' ')

# i = int(input('Enter number: '))
# if i < 20:
#     while i <= 20:
#         print(i, end=' ')
#         i+=1
# elif i > 20:
#     while i >= 20:
#         print(i, end=' ')
#         i-=1

number = int(input("Enter number :"))#5
if number < 0 or number > 10:
    print( "Error")
else:
    i = 1
    while i <= 10:
        print(i, 'x', number, i*number)
        i+=1

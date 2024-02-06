

# def showAllNumber(a,b):
#     print(a, b)
    
# showAllNumber(5,9)

def sumAllNumber( 
                #  start, 
                #  end,
                 *args ):
    #args[0] = 1000 - error   
    # temp = list(args)
    # print(temp)
    # print(f"Count elements in cortege {len(args)}")
    # print(f"Count element [5] in cortege {args.count(5)}")
    # print(f"Index element [5] in cortege [{args.index(5)}]")
    # for elem in args:
    #     print(elem, end=" ")
    # print()
    # print(f"First element {args[0]}") 
    for i in range(len(args)):
        print(args[i], end=" ")
    print()    
    # print(f"Start = {start}. End = {end}")
    # return sum(args)

res = sumAllNumber(10,8,9,6,7,4,12,5,5,5)
# print(f'Res = {res}')

# print(2,7,8,9,"Hello", '\n',78,100,120,333,999)

#lambda function

# def summa(a,b):
#     return a+b

# def show(color):
#     print(color)
    
# print(summa(10,20))
# show("red")

# lambda_show = lambda color:print(color)
# lambda_show("green")

# lambda_summa = lambda a,b:a+b#return a+b
# print(lambda_summa(5,8))

# def doubleNumbers(number, a):#
#     #number= []
#     # a = 10
#     a+= 10
#     for i in range(len(number)):
#         number[i] = number[i]*2
#     #print(a)
#     print(f"id (a) {id(a)}")
#     print(f"id (numbers) {id(number)}")
# numbers = [4,7,8,9,12,3,6,5,2,3,11,77]
# print(numbers)

# a = 2  
# print(a) 
# print(f"id (a) {id(a)}")
# print(f"id (numbers) {id(numbers)}")
# doubleNumbers(numbers, a)
# print("---------------------------------------------")
# print(numbers)


# line = input("Enter numbers : ").split(" ")
# line = [int(elem) for elem in line ]
# print(line)

# numbers = [4,7,8,9,12,3,6,5,2,3,11,77]

        

# def double(x):
#     return x*2
# def pow(x):
#     return x**2
# def increment(x):
#     return x+1
#res = list(map(double,numbers)) 
# res = list(map(lambda x:x*2,numbers)) 
# print(res)
# #res = list(map(pow,numbers)) 
# res = list(map(lambda x:x**2,numbers)) 
# print(res)
# #res = list(map(increment,numbers)) 
# res = list(map(lambda x:x+1,numbers)) 
# print(res)

# line = list(map(int, input("Enter numbers : ").split(" "))) 
# print(line) 

# res = list(filter(lambda x:x%2==0,numbers))
# print(res)

# res = list(filter(lambda x:x> 0 and x < 6,numbers))
# print(res)

# colors = ['red', 'green', 'blue','purple','pink','black','lime','cyan','grey']

# # def checkColor(color):
# #     if len(color)== 4:
# #         return True
# #     else:
# #         return False
# def checkColor(color):
#     return len(color)== 4
    
# print(colors)
# #new_colors = list(filter(checkColor, colors))
# new_colors = list(filter(lambda color:len(color)== 4 , colors))
# print(new_colors)


# numbers = [1,2,3,4]
# #4! = 1*2*3*4

# for elem in numbers:#1! 2! 3! 4! 
#     factorial = 1
#     for i in range(1,elem+1):#1 2 3 4
#         factorial*=i#1 * 2 *3*4
#     print(factorial)
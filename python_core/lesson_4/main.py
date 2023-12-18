# a = 5
# b = 7
# c = 10

'''
print (a, b, c)
print ("Number a = {}". format(a))
print ( "Number b = {}". format (b))
print ("Number c = {}". format (c))
print ("Number a = {}. b = {}. c = {}". format(a, b,c))
print ("Number a = {}. b = {}. c = {}". format(c,b,a))
print(f"Numbers : a = {a} . b = {b}. c = {c}")
'''

import math
print (math. ceil (2.5))
print(math. floor (2.5))
print (math.pow(2,3))
print (math.sqrt (16))

import random
print( random.random ())        #0.0....1.0
print(random.randint (0,1))     #0....1 • 1
print (random.randint(0,1000))  #0. 1000
print (random.randint(20,25))   #20. 50

month = int(input("Enter number of month :"))#key
match month: #2
  case 1:
    print ("January")
  case 2:
    print ("February")
  case 3:
    print ("March")
  case _:
    print ("Error")
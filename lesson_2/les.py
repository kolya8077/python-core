# Завдання 1

numOne = int(input('Ведіть перше число: '))
numTwo = int(input('Ведіть друге число: '))
numThree = int(input('Ведіть третє число: '))

resultSum = numOne + numTwo + numThree
resultProd = numOne * numTwo * numThree

print(f'Сума чисел = {resultSum}, добуток чисел = {resultProd}')

# Завдання 2

numOne = int(input('Ведіть зарплату: '))
numTwo = int(input('Ведіть місячний платіж: '))
numThree = int(input('Ведіть комунальний платіж: '))

result = numOne - numTwo - numThree

print('Залишок заробітньої платні: ', result)

# Завдання 3

diagonalOne = int(input('Діагональ a: '))
diagonalTwo = int(input('Діагональ b: '))

res = (diagonalOne * diagonalTwo) / 2

print('Площа ромба = ', res)

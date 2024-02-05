
# line = "Lorem ipsum dolor"
# print(id(line))
# line+= "!!!"
# print(id(line))

# print(line[0])
# print(len(line))#size = 20 . index first = 0. index last = 19
# print(line[-len(line)])

# print(line[19])
# print(line[len(line)-1])

# print(line[0:5])
# print(line[-5:-1])
# print(line[:7])#start = 0
# print(line[:-2])
# print(line[5:])
# print(line[:])
# print(line[2: :2])
# print(line[::2])
numbers = "123456789"
letters = "lkgfdrtyu"
line = "Lorem Ipsum is dummy text often text used in text printing text and text web design."
word = "Fruit Apple"
message = "BANANA"
letterDigit = "123hyt96dffg"

# print("======================= isalnum()================")
# print("\t", numbers, "---->", numbers.isalnum())
# print("\t", letters, "---->", letters.isalnum())
# print("\t", line, "---->", line.isalnum())
# print("\t", word, "---->", word.isalnum())
# print("\t", message, "---->", message.isalnum())
# print("\t", letterDigit, "---->", letterDigit.isalnum())
# print("=================================================")

# print("======================= isalpha()================")
# print("\t", numbers, "---->", numbers.isalpha())
# print("\t", letters, "---->", letters.isalpha())
# print("\t", line, "---->", line.isalpha())
# print("\t", word, "---->", word.isalpha())
# print("\t", message, "---->", message.isalpha())
# print("\t", letterDigit, "---->", letterDigit.isalpha())
# print("=================================================")
# print("======================= isdigit()================")
# print("\t", numbers, "---->", numbers.isdigit())
# print("\t", letters, "---->", letters.isdigit())
# print("\t", line, "---->", line.isdigit())
# print("\t", word, "---->", word.isdigit())
# print("\t", message, "---->", message.isdigit())
# print("\t", letterDigit, "---->", letterDigit.isdigit())
# print("=================================================")
# print("======================= isspace()================")
# print("\t", numbers, "---->", numbers.isspace())
# print("\t", letters, "---->", letters.isspace())
# print("\t", line, "---->", line.isspace())
# print("\t", word, "---->", word.isspace())
# print("\t", message, "---->", message.isspace())
# print("\t", letterDigit, "---->", letterDigit.isspace())
# print("=================================================")
# print("======================= islower()================")
# print("\t", numbers, "---->", numbers.islower())
# print("\t", letters, "---->", letters.islower())
# print("\t", line, "---->", line.islower())
# print("\t", word, "---->", word.islower())
# print("\t", message, "---->", message.islower())
# print("\t", letterDigit, "---->", letterDigit.islower())
# print("=================================================")
# print("======================= isupper()================")
# print("\t", numbers, "---->", numbers.isupper())
# print("\t", letters, "---->", letters.isupper())
# print("\t", line, "---->", line.isupper())
# print("\t", word, "---->", word.isupper())
# print("\t", message, "---->", message.isupper())
# print("\t", letterDigit, "---->", letterDigit.isupper())
# print("=================================================")
# print("======================= istitle()================")
# print("\t", numbers, "---->", numbers.istitle())
# print("\t", letters, "---->", letters.istitle())
# print("\t", line, "---->", line.istitle())
# print("\t", word, "---->", word.istitle())
# print("\t", message, "---->", message.istitle())
# print("\t", letterDigit, "---->", letterDigit.istitle())
# print("=================================================")
# print("======================= lower()================")
# print("\t", numbers, "---->", numbers.lower())
# print("\t", letters, "---->", letters.lower())
# print("\t", line, "---->", line.lower())
# print("\t", word, "---->", word.lower())
# print("\t", message, "---->", message.lower())
# print("\t", letterDigit, "---->", letterDigit.lower())
# print("=================================================")
# print("======================= upper()================")
# print("\t", numbers, "---->", numbers.upper())
# print("\t", letters, "---->", letters.upper())
# print("\t", line, "---->", line.upper())
# print("\t", word, "---->", word.upper())
# print("\t", message, "---->", message.upper())
# print("\t", letterDigit, "---->", letterDigit.upper())
# print("=================================================")
# print("======================= capitalize()================")
# print("\t", numbers, "---->", numbers.capitalize())
# print("\t", letters, "---->", letters.capitalize())
# print("\t", line, "---->", line.capitalize())
# print("\t", word, "---->", word.capitalize())
# print("\t", message, "---->", message.capitalize())
# print("\t", letterDigit, "---->", letterDigit.capitalize())
# print("=================================================")
# print("======================= title()================")
# print("\t", numbers, "---->", numbers.title())
# print("\t", letters, "---->", letters.title())
# print("\t", line, "---->", line.title())
# print("\t", word, "---->", word.title())
# print("\t", message, "---->", message.title())
# print("\t", letterDigit, "---->", letterDigit.title())
# print("=================================================")
# print("======================= swapcase()================")
# print("\t", numbers, "---->", numbers.swapcase())
# print("\t", letters, "---->", letters.swapcase())
# print("\t", line, "---->", line.swapcase())
# print("\t", word, "---->", word.swapcase())
# print("\t", message, "---->", message.swapcase())
# print("\t", letterDigit, "---->", letterDigit.swapcase())
# print("=================================================")

# print("\t", line, "---->", line.find('used'))
# print("\t", line, "---->", line.find('text'))
# print("\t", line, "---->", line.find('text',22))
# print("\t", line, "---->", line.find('text',33))
# print("\t", line, "---->", line.find('text',46))
# print("==========================================")
# index = -1
# while True:
#     index = line.find('text',index + 1)
#     if index == -1:
#         break
#     print("\t", line, '----->', index)
# print("==========================================")
# print("\t", line, "---->", line.rfind('text'))
# print("\t", line, "---->", line.find('text  '))
# #print("\t", line, "---->", line.index('text  '))
# print("\t", line, "---->", line.rindex('text',0,25))
# print("\t", line, "---->", line.count('text'))
# print("\t", line, "---->\n\t", line.replace('text','yellow',2))

# print("\t", line, "---->\n\t", line.startswith("L"))
# print("\t", line, "---->\n\t", line.startswith("A"))
# print("\t", line, "---->\n\t", line.startswith("I",6,10))
# print("\t", line, "---->\n\t", line.endswith('!'))
# print("\t", line, "---->\n\t", line.endswith('.'))


# message = 'Python 2024'
# print(message.center(50))
# print(message.center(5))
# print(message.ljust(30))
# print(message.ljust(30,'@'))
# print(message.rjust(30))
# print(message.rjust(30,'@'))
# message = '          Python 2024        '
# print(message.lstrip())
# print(message.rstrip())
# print(message.strip())
# message = '@;          Python 2024        @'
# print(message.lstrip('@;'))
# print(message.rstrip('@'))
# print(message.strip('@'))
# number = "123"
# print(number.zfill(5))
# number = "+123"
# print(number.zfill(5))








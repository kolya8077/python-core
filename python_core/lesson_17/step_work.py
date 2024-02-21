# #open file
# #read file
# #write file
# #close file
# url = r"C:\Users\helen\Desktop\Python_PV_311\19_WorkWithFile\my.txt"
# #file = open("19_WorkWithFile/my.txt")
# # file = open(url)#mode = r - read
# # #print(file.read())
# # #print(file.readline().strip())
# # #print(file.readlines())
# # print(file.read(10))
# # file.close()
# # with open(url) as file:
# #     print(file.read())
# #     print(type(file.read()))
#     #file.close()
# # print(type(5))  
# # print(type(5.333))  
# # print(type('s'))  
# # print(type("type"))  
# # print(type(True))  
# url_write = "19_WorkWithFile/write.txt"
# # with open(url_write,'a') as file:
# #     file.write("Hello world\n")
    
# # with open(url_write,'w') as file:
# #     file.write("")

# lines = ['Sed volutpat nisi in vestibulum congue.',
#     'Cras dapibus tellus nec pulvinar eleifend.',
#     'Curabitur nec mi semper, accumsan leo sit amet, fringilla tortor.'
# ]
# # with open(url_write,'w') as file:
# #     #file.write(lines[0])
# #     counter = 1
# #     for line in lines:
# #         file.write(f"{counter}. {line}\n")
# #         counter+=1
# # with open(url_write,'w') as file:
# #     file.writelines(i + "\n" for i in lines)
        
# # def readFile(fname):
# #     with open(fname,'r') as file:
# #         return file.read()
    
# # def appFile(fname, info):
# #     with open(fname,'a') as file:
# #         file.write(info)

# # url_1 = "19_WorkWithFile/write.txt"
# # url_2 = "19_WorkWithFile/my.txt"

# # text = readFile(url_1)
# # appFile(url_2,text)

# # lines = []
# # with open("19_WorkWithFile/my.txt") as file:
# #         lines = file.readlines()
# # with open("19_WorkWithFile/write.txt",'a') as file:       
# #     for line in lines[::-1]:
# #         file.write(line.strip() + "\n")
        
# # with open("19_WorkWithFile/my.txt",'a') as file:
# #         # print(file.readable())
# #         # print(file.writable())
# #         file.write(str(555))
# # import re
# # line = ''
# # with open("../19_WorkWithFile/my.txt") as file:
# #         line = file.read()
        
# # print(line.count("\n"))

# # print(re.split("[,.? ]", line))
# # words = re.split("[,.? ]", line)
# # for word in words:
# #     if len(word) >= 7:
# #         print(word)
    
# url_write = r"..\Python_PV_311\19_WorkWithFile\write_test.txt"
# with open(url_write,'a') as file:
#     file.write("Hello world\n")

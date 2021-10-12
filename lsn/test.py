# num = 7
# if num > 3:
#     print("3")
#     if num < 5:
#         print("5")
#         if num == 7:
#             print("7")

####################
# list = [2, 3, 4, 5, 6, 7]

# for x in list:
#     if(x % 2 == 1 and x > 4):
#         print(x)
#         break

# for i in range(10):
#     if not i % 2 == 0:
#         print(i+1)

#########################
# def ex(a, b):
#     return a / b


# try:
#     a = "2"
#     b = 0
#     ex(a, b)
# except (ZeroDivisionError, TypeError):
#     print("zero division error or type error")

##############
file = open("text.txt", "r")
# cont = file.read()
# print(cont)
# file.close()
print(file.read(1))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

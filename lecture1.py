# VARIABLES
# x=1.23
# y=2+3j
# print(type(x))
# type(y)


# #single line comment
"""print(multiline comment)"""
'''print(multiline comment pt.2)'''

# print(int(x))
"""you can't write print(int(y)) as this only works for bytes or real numbers, not complex"""

#INPUT AND OUTPUT
# nam=input("What's your name?")
# print("my Name is = ", nam)

#CONDITIONAL STATEMENTS
'''1. if'''
# age=19
# if age>=18:
#     print("adult")

# '''2. if else'''
# if age>=18:
#     print("adult")
# else:
#     print("not adult")

'''3. elif'''
# if age<=12:
#     print("Child")
# elif age<=19:
#     print("Teenager")
# else:
#     print("Adult")

'''4. ternary'''
# x=20
# s="big number" if x>50 else "small number"
# print(s)

'''5. Match Case'''
# match x:
#     case 10:
#         print("10 it is")
#     case 20|30:
#         print("20 or 30, it is")
#     case _:
#         print("idk not imp much")

    #similar to switch case, don't require break like it does in C
#FUNDAMENTALS

# VARIABLES
x=1.23
y=2+3j
print(type(x))
type(y)

abc, defg, hij = 1, 2, 3
print(abc, defg, hij)

#Swap variables without temp
abcd = 5
bcde = 9
abcd, bcde = bcde, abcd
print(abcd, bcde)  # Output: 9 5


# #single line comment
"""print(multiline comment)"""
'''print(multiline comment pt.2)'''

#TYPE CONVERSION
print(int(x))
"""you can't write print(int(y)) as this only works for bytes or real numbers, not complex"""

#INPUT AND OUTPUT
nam=input("What's your name?")
print("my Name is = ", nam)

#CONDITIONAL STATEMENTS
'''1. if'''
age=19
if age>=18:
    print("legally adult")

'''2. if else'''
if age>=18:
    print("can vote")
else:
    print("can't vote")

'''3. elif'''
if age<=12:
    print("Child")
elif age<=19:
    print("Teenager")
else:
    print("Adult")

'''4. ternary'''
x=20
s="big number" if x>50 else "small number"
print(s)

'''5. Match Case'''
match x:
    case 10:
        print("10 it is")
    case 20|30:
        print("20 or 30, it is")
    case _:
        print("idk not imp much")

    #similar to switch case, don't require break like it does in C

'''6. if AND, if OR'''
a=23
b="yes"
if a>=18 and "yes"==b:
    print("Permission granted")
else:
    print("Permission Denied")

s="python"
if "python"==s or "java"==s:
    print("okay")
else:
    print("cool")

#LOOPS

'''1. while loop'''
count = 0
while (count < 3):
    count+= 1
    print(count)

'''2. while-else loop'''
i=1
while (i<5):
    i+=1
    print(f"the number is {i}")
    '''when using f-string, the variable inside {} gets converted to a string automatically only for display, 
    but the variable itself doesn't change.'''
else:
    print("In Else Block")

'''3. for loop'''
n = 4
for j in range(0, n):
    print(j)

for letter in 'thebigblackhorse':
    if letter == 'e' or letter == 's':
        continue
print('Current Letter :', letter)

for letter in 'the cutebluecat':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)
#there is no do while loop in python, it can made using conditional statements in while loop
#YET TO STUDY IN LOOPS : List, Tuple, String, and Dictionary Iteration Using for Loops in Python
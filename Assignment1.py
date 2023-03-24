import math
#########################HelloWorld
print("Hello World!")
#########################BMI
w = float(input("Please enter your weight (kg)"))
h = float(input("Please enter your Height (m)"))

BMI = w / h**2

print('Your Body mass index is :', BMI)

if BMI < 18.5:
    print('You are Underweighted')
elif BMI > 18.5 and BMI < 24.9:
    print('Good job, You are normal')
elif BMI > 25 and BMI < 29.9:
    print('You are Overweighted')
elif BMI > 30 and BMI < 34.9:
    print('You are Fat')
else:
    print('How are you?')
##########################StudentScores
x = input("First name: ")
y = input("Last name: ")
a = float(input('Please enter your first Score: '))
b = float(input('Please enter your second Score: '))
c = float(input('Please enter your third Score: '))
m = (a+b+c)/3
print('Your moaddel is:', m)

if m >= 17 and m <= 20:
    print("Good job ",x," You are Gr8!")
elif m < 17 and m >= 12:
    print("You are normal mr.", y)
elif m<12:
    print("You FAILED")
#############################PossibleTriangle
print("enter 3 numbers to see if there is a Triangle with the same dimentions! ")
a = int(input("side 1:"))
b = int(input("side 2:"))
c = int(input("side 3:"))
if (a + b) < c or (a + c) < b or (b + c) < a:
    print('this TRIO is not possible!')
else:
    print('It is possible!')

############################Calculator
print("welcome to the Calculator!")

print('choose the operations: \n', '+, -, *, /, Jazr, sin, cos, tan, cot, factorial as !')
o = input()

a = float(input("Enter First Number"))
b = float(input("Enter Second Number"))

if o == "+" :
    result = a + b
elif o == "-":
    result = a - b
elif o == "*":
    result = a * b
elif o == "/":
    result = a / b
elif o == "jazr":
    result = math.sqrt (a)
elif o == "sin":
    a = a * (math.pi/180)
    result = math.sin(a)
elif  o == "tan":
    a = a * (math.pi/180)
    result = math.tan(a)
elif o == "cot":
    a = a * (math.pi/180)
    result = math.cos(a) * math.sin(a)
elif o == "!":
    result = math.factorial(a)

print(result)








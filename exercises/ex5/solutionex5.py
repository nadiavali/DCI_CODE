# Task 1 - calculate sum
print("\n---TASK 1--- \n")

first = int(input("First number: "))
second = int(input("Second number: "))
third = int(input("Third number: "))

result = first + second + third

if first == second and second == third:
    result = 3 * result
    print("The triple sum is: ", result)
else:
    print("The sum is: ", result)


# Task 2 - get the difference
print("\n---TASK 2--- \n")

first = int(input("First number: "))
second = int(input("Second number: "))

if first > second:
    result = 2 * (first - second)
else:
    result = abs(first - second) 

print("The result of calculation is ", result)


# Task 3 - odd or even number
print("\n---TASK 3--- \n")

number = int(input("Number to check: "))
mod = number % 2

if mod > 0:
    print(number, "is an odd number!")
else:
    print(number, "is an even number!")


# Task 4 - circle area
print("\n---TASK 4--- \n")

from math import pi

radius = float(input("Input the radius of the circle : "))
area = round(pi * radius**2, 2)  # rounding to two decimals
print ("The area of the circle with radius ", radius, " is: ", area) 


# Task 5 - guess a number

print("\n---TASK 5--- \n")
target_num = 7  # hard-coded version
guess_num = None
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


# Task 6 - Celsius to Fahrenheit conversion

print("\n---TASK 6--- \n")

scale = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")
temp = input("Input the value of temperature you'd like to convert  : ")

temp = int(temp)

if scale == "C":
  result = int(round((9 * temp) / 5 + 32))
  o_convention = "Fahrenheit"
elif scale == "F":
  result = int(round((temp - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention!")
print("The temperature in", o_convention, "is", result, "degrees.")


# Task 7 - pattern

print("\n---TASK 7--- \n")


print('* ',2 * '* ', 3 * '* ', 4 * '* ', sep='\n')
n=5

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')


# Task 8 - Fibonacci series

print("\n---TASK 8--- \n")
x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x+y

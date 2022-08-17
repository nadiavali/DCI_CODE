# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
#task1
three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)

#task2
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)

#task3

n = 5
sum = 0
for num in range(n+1):
    sum += num
print("Sum =", sum)

#task4
for x in range(3):
    print(x)

for j in range(5):
    print("This is loop number j", j)

x=10
while x > 0:
    print(x)
    x -= 1
    
x = 10
countdown = 5
while countdown :
    print(countdown)
    countdown -= 1

print("Start!")

#task5

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x==z:
    result = 0
    print('calculated sum is', result)
else:
    sum = x + y + z
    print("Calculated sum is ", sum)

#task6

x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result > 15 and result < 20:
    result= 20
print("Calculated sum is ", result)

#task7

a = str(input("First value: "))
b = str(input("Second value: "))

print("Before swapping: ",a,b )

temp = a
a = b
b = temp
print("After swapping:" , a,b)

#task8

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))

#task9
x = int(input("Type your value:"))

if x == 0:
    x=False
elif x ==1:
    x =True
else:
 pass

print("Your entered value is now ", x)

#task10
x = int(input("First number: "))
y = int(input("Second number: "))

if x %y == 0:
    print("First number is divisible by second number, result =", x // y)
elif y %x == 0:
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisible!")
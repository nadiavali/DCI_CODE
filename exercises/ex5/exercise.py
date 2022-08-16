# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#task1


x,y,z = int(input('num1')),int(input('num2')),int(input('num3'))


if x != y != z :
    print(x+y+z)
    
if x == y ==z:
    print(3*(x+y+z))
    
#task2

n,m = int(input('num1')), int(input('num2'))

if n>m :
    print(2*(n-m))
        
else:
    print(abs(n-m))

#task3

x = int(input('num'))

if x%2 == 0:
    print(x,'is a even num')
else:
    print(x, 'is a odd num')

#task4
from math import pi
import math
x = float(input('radius'))
a = (pi*(x**2))
print('area is', round(a,2))

#task5
 
for i in range(11):
    m= 9
    n = int(input('num'))
    if n!=m:
        print(n)
    else:
        print('well done!')
        break

#task6

temp,tempCon = int(input('Please enter a temperature')), str(input('for Fahrenheit enter f, and for Celsius enter c'))
if tempCon == 'c' :
    print((temp*1.8)+32)
else:
    print((temp-32)/1.8)

#task7

m=print( '* \n'+2*'*'+3*'*'+4*'*'+5*'*')
z=print(2* '*')
l=print(3* '*')
s=print(4* '*')
j=print(5* '*')

y=5
for i in range(y,0,-1):
    for m in range(i):
      print('*', end='')
print('')

#task8

x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x+y sum = n+1
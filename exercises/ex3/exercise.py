# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#task1

for i in range(3):
    x =int(input('Enter number:'))
    if x % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
        
#task2

x= int(input('num'))
if x==1 :
        m=int(input('another'))
        for i in range(m+1):
            print(i)
elif x==2 :
    s=int(input('another'))
    n=int(input('another'))
    for i in range(s,n):
            print(i) 
elif x==3 :

    f= int(input('another'))
    h=int(input('another'))
    d= int(input('another'))
    for i in range(f,h,d):
        print(i)



#task3


x= int(input('give me a number!'))
for i in range(1,x+1):
    if x % i== 0 :
        print(i)

#task4

x = int(input('num'))

if x>1:
    for i in range(2,x):
        if  x%i ==0 :
            print('not prime')
            break
    else:
        print('prime')

#task5


for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
        
    elif i%5 == 0:
        print('Buzz')
        
    elif i%3 == 0:
        print('Fizz')
    else:
        print(i)
        
#task6

for i in range(1000,2001):
    if i%7 ==0 and not i%5==0:
        print(i)

# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#task1
# n=0
# while n < 3:
#     x,y=input('num1:'),input('num2:')
#     if x > y:
#         print('num1 is greater!')
#     elif x<y:
#         print('num2 is greater!')
#     elif x==y:
#         print('num1 is equal to num2')
#     elif x>=y:
#         print('num1 is equal or greater than num2')

#     n += 1
    

#task2

l1 =['January','February','March','April','May','Jun','July','August','September','October','November','December']
l2 =[31,28,31,30,31,30,31,31,30,31,30,31]
y= input('month:')

count=0
for i in l1:
    if y.lower() == i.lower():
        print('the month has days', l2[count])
        break
    count += 1
if count > 11:
    print('error')
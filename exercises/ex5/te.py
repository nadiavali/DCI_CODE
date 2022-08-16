# 0,1,1,2,3,5,8,13,21,34

a,b = 0,1
sum= a+b
print(a)
print(b)
print(sum)
while sum < 50:
    a,b= b,sum
    sum = a+b
    print(sum)
    if b+sum > 50:
        break

numbers = [42, 123]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])
# for i in []:
#     print('never happens')

# for x in []:
#     print('This never happens.')
#numbers[2] = 32 # it will show an error out of range for this reason we need to use append
# numbers.append(32)
# print(numbers)
# numbers.sort() #sort from low to high
# t = numbers.sort() #most of list method are void = their answer is none (dnt assign them)
# print(numbers)
# print(t)

# def add_all(numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total 
# print(add_all(numbers))
# # or
# print(sum(numbers))

t = ['a','b','c','A']
def cap_all():  #you can add t
    res = []
    for i in t:
        res.append(i.capitalize())
    return res

print(cap_all())  # you can add t

def only_upper(t):
    res = []
    for i in t:
        if i.isupper():
            res.append(i)
    return res
print(only_upper(t))

print(t)

x = t.pop() # without index it will delete last element(work with index)
print(t)

del t[1] #work with index
print(t)

t.remove('a') # know the element want to be removed not index and the answer in None
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']

del t[1:3]
print(t)
s ='spam'
t =list(s)
print(t) # break a sting to a list of chars

s = 'This, is, a wonderful night!' #break string into words
t = s.split() #if there is any white space it turns the two word in between into a list
print(t)

s = 'spam,spam,spam'
delimiter = ','# it can be any thing here instead of space
t = s.split(delimiter)
print(t)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '  # it is opposite of split # delimiter here is a space
s = delimiter.join(t)
print(s)

a = [1, 2, 3]
b = [1, 2, 3] # they do not have the same identical #false
a is b

b = a 
b is a # true # reference # association of a variable with an object
# An object with more than one reference has more than one name, so we say that the object
# is aliased.
# If the aliased object is mutable, changes made with one alias affect the other:
# with mutable objs like list avoid aliasing, with immutable objs like strs it is ok
a = 'banana'
b = 'banana'
a is b # true

fruit_colors = {
    "apple": "red",
    "berries": "blue"
}
#Print keys, values, items in a for loop.
for key, value in fruit_colors.items():
    print(key)
    print (value)
    print('='*10)
for a in fruit_colors.items():
    x , y  = a
    print(x)
    print(y)
#immutable
# global_var = 'it is global'
# print(id(global_var))
# def func(global_var):
#     print(id(global_var))
#     global_var = 'did it change'
#     print(id(global_var))
#     return global_var

# print(func(global_var))
# print(global_var)

#mutable
#do it in terminal

def test(l=[]):
    print(id(l))
    l.append(2)
    print(l)
test()

# To assign a default value to a mutable
# argument we have to define it as None
# and do the assignment manually.
# This way, Python creates a new object
# every time. s48 function rose
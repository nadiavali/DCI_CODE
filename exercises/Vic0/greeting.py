# Never name the variable in a fun same as fun name
# def math_op(x, y, opp):
#     if opp == '+':
#         result = f'{x + y} is a addition'
#     elif opp == '-':
#         result = f'{x - y} is a subtraction'
#     elif opp == '*':
#         result = f'{x * y} is a multiplication'
#     else:
#         if y == 0:
#             return 'This is not possible' # it will be an error and we put an exception
#         else:
#             result = f'{x / y} is a division'
#     return result



# Calling the functions

# print(math_op(5,0,'/'))




from dataclasses import replace


names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]
# 
# using an index, replace "Peer" with "Malcom X"

# Add two names to the list of names

# Experiment with the methods in a list using dir(names)

names[-1]= 'Malcom X'
index = names.index('Peer')
names[index] = 'Malcom X'
print(names)

names.append('Nadia')
names.append('Wojciech')
names.append('Michel')
print(names)

names.sort()
print(names)

num = [1, 2, 3]
names.extend(num)
print(names)

names.insert(1,'super')
print(names)

count = names.count('Nadia')
print(count)

removed_element = names.pop(4)
print(removed_element)
print(names)

names.reverse()
print(names)

names.remove('Peter')
print(names)

index = names.index('Nadia')
print(index)

names.clear()
print(names)
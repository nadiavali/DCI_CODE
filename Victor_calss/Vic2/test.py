my_tuple = ("Nadia", [8, 4, 6], (1, 2, 3))
tuples = 'Vali', 1, 2
print(tuples)
print(tuples[1] == 'Man')
print(type(my_tuple))
print(my_tuple[0])

print(my_tuple)

def gender(g, f, l):

    if g == 'female':
        return f'Good morning Ms.{f}!'
    else:
        return f'Good morning Mr.{f}!'

print (gender('female', 'Nadia', 'Vali'))


n = [1, 2, 3, 5, 1, 2, 3, 51, 2, 3, 51, 2, 3, 51, 2, 3, 5]

for i in n[::-1]:
    print(i)



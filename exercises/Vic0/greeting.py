# Never name the variable in a fun same as fun name
def math_op(x, y, opp):
    if opp == '+':
        result = f'{x + y} is a addition'
    elif opp == '-':
        result = f'{x - y} is a subtraction'
    elif opp == '*':
        result = f'{x * y} is a multiplication'
    else:
        if y == 0:
            return 'This is not possible' # it will be an error and we put an exception
        else:
            result = f'{x / y} is a division'
    return result



# Calling the functions

print(math_op(5,0,'/'))

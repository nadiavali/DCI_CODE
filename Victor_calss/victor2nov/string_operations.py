# TODO:
# - Write a function to make two names titlised e.g. title_name(name1, name1)
# - write a function, when given a list of names, it creates one name (test it too) e.g. join_names([‘name1’, ‘name2’, ‘name3’])
#Call your file string_operations.py

def title_name(name1, name2):
    x = name1.title()
    y = name2.title()
    return x, y

def join_names(l):
    m = ' '.join(l)
    return m


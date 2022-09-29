# greetings = {'key1':'man','key2':'Nadia','key3':'love'}
# print(greetings)
# print(greetings['key1'])

# last_name = {1:'Dalton',
# 2:'Rasmussen'
# }
# # "Pass by reference" variables can change
# def full_name(last_name):
#     # variations 
#     last_name[1] = "Hoffmann"
#     last_name[2] = 'Vali'
#     return F'''one family name: {last_name[1]} \nother family name: {last_name[2]}'''



# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)
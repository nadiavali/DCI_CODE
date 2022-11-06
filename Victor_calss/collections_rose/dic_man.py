# template = dict.fromkeys(("street", "number", "zip", "city", "country") ,"Unknown") #unknown is optional
# print(template)

# address = template.copy()
# print(address)

# address.update({'street':'Hogwarts'})
# print(address)
# user = {'john': {'name': 'John Doe'}}
# print(user['john'])
# print(user.get('john'))
# print(user.get('salary'))
# print(user.get('salary', 0.33))
# print(user)

# user.setdefault('mario',{'name': 'mario sanchez'}) # if it does not exist it 
# #will create default value and default key
# print(user)

# user.setdefault('mario',{'name':'man'})
# print(user)

# user['john']['age'] = 28
# print(user)

# user['mario']['age'] = 29
# print(user)

# template.update(user) # merging two dicts
# print(template)

# print(user.popitem()) #remove last item no argument and 

# print(user)

# print(template.pop('zip')) #remove the value of the passed key and return the value
# print(template)

# print(template.keys())
# #dict_keys(['street', 'number', 'city', 'country', 'john', 'mario'])

# print(template.values())

# print(template.items())


'''methods of dict'''
#setdefault #update #copy #fromkeys
#pop #popitem #clear
#get
#items #key #values


# dict1 = {"c": 2, "b": 1, "a": 3}
# print(sorted(dict1)) # sort the keys
# print(sorted(dict1.values())) #sort the values
# print(sorted(dict1, reverse=True)) # sort and then reverse it(default of reverse is false)

dict1 = [
{"name": "John", "age": 31},
{"name": "Mary", "age": 46},
{"name": "Lucy", "age": 25}
]

by_age = lambda user : user['age']
by_name = lambda user: user["name"]


print(sorted(dict1, key=by_age))
print(sorted(dict1, key=by_name))


#The function any will return True only if
#any of the values in the iterable is truthy

# The function all will return True only if
# all the values in the iterable are truthy

a_list1 = [1, True, "Mary", {1, 2}]
print(bool(a_list1), any(a_list1), all(a_list1)) 

a_list2 = [1, True, "Mary", {}]
print(bool(a_list2), any(a_list2), all(a_list2))

a_list3 = [0, False, "", {}] # they are all falsey
print(bool(a_list3), any(a_list3), all(a_list3))


from collections import OrderedDict

a_dict = {"name": "Mary", "age": 54}
ordered = OrderedDict(a_dict)
print(ordered)

ordered.move_to_end("name")
print(ordered)


from collections import ChainMap
root = {"a": 1, "b": 2}
adjust1 = {"b": 3, "c": 4}
chain = ChainMap(adjust1, root)
print(chain)

print(dict(chain))

print(chain['b'])

print(chain.maps) # list of input to manipulate 
chain.maps[0]['a'] = 100
print(chain.maps)



# A ChainMap is a dictionary-
# like object and can also be
# used as an argument of
# another ChainMap.

root = {"a": 1, "b": 2}
adjust1 = {"b": 3, "c": 4}
adjust2 = {"c": 5, "d": 6}
chain1 = ChainMap(adjust1, root)
chain2 = ChainMap(adjust2, chain1)
print(chain2)



# A namedtuple creates a
# new custom data type
# with the name and
# attributes indicated.
# It requires a string for the
# name of the type and a list
# of attributes

from collections import namedtuple
Address = namedtuple('Address', ['street', 'number', 'city', 'county'])
home = Address('Jahanara', 16, 'Shiraz', 'Iran')
print(home)

print(home[0])
print(home.number)
print(home.county)


# The objects created this
# way are tuples, they do not
# allow changing the values
# or adding new keys.

#home[0] = "Somewhere else" TypeError


print(home._asdict()) #turn it into dict
print(home._replace(number=6))
print(home)
# # To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop

# # def total_list(lst):
# #     total = 0
# #     for item in lst:
# #         total += item
# #     return total
# # # test case
# # print(total_list([1,2,3]))   # answer is 6

# # def total_list(lst):
# #     l = 0
# #     total = 0
# #     while l <len(lst):
# #        total += lst[l]
# #        l += 1
# #     return total
# # print(total_list([3,3,3])) 

# con = ['Iran', 'Germany', 'Britain']
# # for c in con:
#     # con += con
#     # print(con)

# def country(con):
#     cont += cont[l]
#     l = 0
#     while l < len(con):
#         l = l + 1
#         cont += con[l]
#         print(cont)
#         l += 1
#         return f'I love {cont}'

# print(country(['Iran', 'Germany', 'Britain']))

# transformer = ['a', 'u', 't', 'o', 'b', 'o', 't', 's']

# a = ''.join(transformer)
# print(a)

# lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]

# print(lists[0][1][0]['name'])
# print(lists[1][2]['age'])



# words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

# words[1:3]=['lion']
# print(words)
# help(words[1:3])
from collections import Counter


fridge = [
 "Apple", "Apple", "Cabbage",
 "Steak", "Cheese", "Apple",
 "Carrot", "Carrot", "Iogurt",
 "Beer"
]

# counter = {}

# for ingredient in fridge:
#     if ingredient not in counter:
#         counter[ingredient] = 0
#     counter[ingredient] += 1

# print(counter)
# counter = Counter(fridge)
# print(counter)
# print(counter.total())
from collections import OrderedDict

a_dict = {"name": "Mary Schmidt", "age": 54, "height": 120}

ordered = OrderedDict(a_dict)

print(ordered)

a_dict.move_to_end("age", last=False)

print(ordered)
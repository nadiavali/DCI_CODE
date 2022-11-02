# # a = dict()
# # print(a)
# # a['one'] = 'uno'
# # print(a)
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# # print(eng2sp)
# # 'one' in eng2sp # you can only use the key for in #true
# # vals = eng2sp.values()
# # print(vals)
# # 'uno' in vals # true # now you can use value for in
# a = 'NadiaVAli'

# def histogram(a):
#     d = dict()
#     for i in a:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d

# print(histogram(a))
# n = histogram('N')
# print(n)
# print(n.get('N', 0))  #1 # 0 is default value for 'N'
# print(n.get('w', 0))
# def print_h(h):
#     for i in h:
#         print(i, h[i])

# print(print_h({'N': 1, 'a': 2, 'd': 1, 'i': 2, 'V': 1, 'A': 1, 'l': 1}))
s = {'n': 1, 'a': 2, 'd': 3, 'i': 4, 'v': 5, 'l': 6}
l = {'n': 1, 'a': 2, 'd': 1, 'i': 3, 'v': 3, 'l': 1}

# for key in sorted(s):
#     print(key,s[key])

# def reverse_lookup(d,v):
#     for key in d:
#         if d[key] == v:
#             return key
#     raise LookupError()

# print(reverse_lookup(s,1))

# def invert_dict(d):
#     invert_d = {}
#     for key in d:
#         v = d[key]
#         if v not in invert_d:
#             invert_d[v] = [key]  #why we put the key in []: so because the key and value got
#             #changed and now we have for example for key 3 for values which they must be in list otherwise 
#             #it will shows an error if you try it with list 's' it does not need [] 
#         else:
#             invert_d[v].append(key)
#     return invert_d

# print(invert_dict(s))

# known = {0:0, 1:1}
# def fibonacci(n):
#     if n in known:
#         return known[n]
#     res = fibonacci(n-1) + fibonacci(n-2)
#     print(res)
#     known[n] = res
#     return res

# print(fibonacci(9))

count = 0
def example3():
    global count  # integers are immutable
    count = count + 1

print(example3())

# If a global variable refers to a mutable value, you can modify the value without declaring
#the variable:
known = {0:0, 1:1}
def example4():
    known[2] = 1

#So you can add, remove and replace elements of a global list or dictionary,
#  but if you want to reassign the variable, you have to declare it:
def example5():
    global known
    known = dict()
    #print(known)
#print(example5())
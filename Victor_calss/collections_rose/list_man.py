# list1 =[1,2,3,4,5]

# list1.sort(reverse=True) # does change the list
# print(list1)
# print(sorted(list1)) # does not change the list
# print(list1)

# list1[0] = 'beer'
# print(list1)
# list1[0:2] = 'wine'
# print(list1)
# list1[0] = None
# print(list1)
# list1[0] =[]
# print(list1)
# list2 = list1.pop(0)
# print(list1)


nums = [1, 2, 3]
eng = ('one', 'two', 'three')

zip1 = zip(eng, nums)
print(zip1)

# for item in zip1:
#     print(item)

# #or

for item in zip(eng, nums):
    print(item)


# map function, that
# applies the given function to each
# element of the given iterable.

a_list = [1, 2, 3, 4, 5]
by_two = lambda num: num * 2
a_list_by_two = map(by_two, a_list) #1.func 2.iterable
#print(a_list_by_two)

print(list(a_list_by_two)) # if you dont add list it won't show you the result


# The filter function returns an iterable
# with the elements of the given iterable
# that match a condition defined in a
# function
# nums = [1, 2, 3, 4, 5]
# is_odd = lambda num: (num % 2) != 0
# odds = filter(is_odd, nums)  # if they match the condition of func # not changing the iterable only filter them
# print(odds)
# print(list(odds))


#counter

from collections import Counter
fridge = ["Apple", "Apple", "Cabbage", "Steak", "Cheese", "Apple",
"Carrot", "Carrot", "yogurt", "Beer"]
counters = Counter(fridge)
# print(counters)
#print(counters.total()) # = print(len(fridge))

lunch = Counter(Cabbage=1,Carrot=2)

counters.subtract(lunch) #subtract lunch from counters
print(counters) # it modifies the original counters


# The minus operator - can also be
# used to obtain a similar result but
# returning a new counter, and not
# changing the original counter


counters = Counter(fridge)
shop = Counter(Carrot=6, Beer=6)
counters.update(shop)
print(counters)

# The plus operator + can also be
# used to obtain a similar result but
# returning a new counter, and not
# changing the original counter


counter = Counter(fridge)
print(counter)

for item in counters.most_common():  # return a list sorted by occurrence in descending
                                        # order that can be iterated in the same order
    print(item) #The items of the list will be tuples containing both the value and the
                #counter of each item.


# Counters can also be used
# with some binary
# operators.

counter = Counter(Apple=1, Cabbage=2)
counter2 = Counter(Cabbage=1, Carrot=2)
print(counter + counter2)

print(counter - counter2)

print(counter & counter2)

print(counter | counter2)

print(counter == counter2)
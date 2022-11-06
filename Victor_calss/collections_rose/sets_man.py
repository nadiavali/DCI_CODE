# they do not allow duplicate values
# Have an no order
# Do not allow their objects to be changed
# But the items themselves can not be sets.
# sets = {{"John", "Mary", "Amy"},{32, 43, 51}} #TypeError
dates = {'datetime', 'datetime'}
datetime = 1
datetime = 2
dates1 = {datetime, datetime}
#in both case it will accept duplicate but it will merge it to one and delete the pervious one
print(dates1) # only print one time datetime

copy = dates.copy()
print(copy)
copy.add('Nadia')
print(copy)
copy.update('nad')
print(copy)

copy.update(['nad','Nadia'])
print(copy)


random = copy.pop()
print(random)
print(copy)

# The discard method removes the
# given value and returns nothing.
# The remove method is like discard
# but it throws an error exception if the
# value does not exist in the set

random = copy.discard('nad')
print(random)
print(copy)


fruits = {"Pear", "Mango", "Apple", "Strawberry"}
smoothie = {"Mango", "Orange", "Pear"}
print(fruits.intersection(smoothie))  # a eshterak b
print(fruits.difference(smoothie))   #a -b

fruits.symmetric_difference(smoothie)  #a ejtema b - a eshterakb
print(fruits)

fruits.symmetric_difference_update(smoothie) #update the fruit
print(fruits)

print(fruits.union(smoothie)) # a ejtema b

smoothie1 = {"Mango"}
print(fruits.isdisjoint(smoothie)) #false if they have a value in common and true if they don't
print(fruits.issubset(smoothie1))
print(smoothie1.issubset(fruits))  #true should be if first set is excatly in second set

set1 = {1, 2, 3}
set2 = {3, 2, 1}
set1 == {1, 1, 2, 2, 3, 3} #true
set1 == set2 #true


#Using set() on both iterables before
#comparing them will remove duplicates and ignore the order

list1 = [1, 2, 3]
list2 = [3, 1, 2, 1, 3, 2]
set(list1) == set(list2) #true


'''methods of sets'''
#add #update
#pop #remove #discard #clear
#copy
#intersection #difference ....


nums = "123"
eng = ("one", "two", "three")
deu = {"ein", "zwei", "drei"}
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]

# for item in zip(nums, eng, deu, cat, fra): #no order for sets
#     print(item)


for num, en, de, ca, fr in zip(nums, eng, deu, cat,
fra):
    print(num + ". " + en, de, ca, fr)
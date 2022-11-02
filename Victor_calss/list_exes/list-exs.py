# Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
# # the elements from all of the nested lists. For example:
# t = [[1, 2], [3], [4, 5, 6]]


# def nested_sum(t):
#     return sum(sum(t,[]))

# print(nested_sum(t))

# Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
# that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# t = [1, 2, 3, 4]
# >>> cum_sum(t)
# [1, 3, 6]
# def cum_sum(t):
#     total = []
#     i = 0
#     for n in t:
#         i += n
#         total.append(i)
#     return total
        
# print(cum_sum(t))

# Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# t = [1, 2, 3, 4, 9, 11]
# # >>> middle(t)
# # [2, 3]

# def middle(t):
#     m = t[1:-1]
#     return m
# print(middle(t))

# Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None . For example:
# t = [1, 2, 3, 4]
# # >>> chop(t)
# # >>> t
# # [2, 3]
# def chop(t):
#     del t[0]
#     del t[-1]
#     return t
# print(chop(t))

# Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False
# t =['a','b','h','c']

# def is_sorted(t):
#     a = t.copy()
#     t.sort()
#     if t == a :
#         return True
#     else:
#         return False

# print(is_sorted(t))

#Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
#Write a function called is_anagram that takes two strings and returns True if they are anagrams.
def is_anagram(t,s):
    a = sorted(t)
    b = sorted(s)
    if a == b:
        return True
    else:
        return False
print(is_anagram('mad','dam'))
#Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
#is any element that appears more than once. It should not modify the original list.
    

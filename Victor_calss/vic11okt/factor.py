# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4))

# for i in range(1000):
#     print(factorial(i), f'i:{i}')

#www.leetcode.com

# l =[1, 1, 2, 6]
# #20 minutes, trying to rewrite this to use a recursive style
# def get_sum(list):
#     total = 0
#     return get_sum(i+ total)

# print(get_sum(l))


# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)

# print(countdown(4))
def print_n(s, n): 
     #print s for n time
    if n <= 0:
        return
    print('s', s)
    print_n(s, n-1)

#print(print_n(2,3))

def do_n(print_n, n):
    if n <= 0:
        return
    print(print_n)
    do_n(print_n, n-1)

print(do_n('hello',3))

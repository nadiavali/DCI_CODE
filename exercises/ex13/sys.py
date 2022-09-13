import sys

n = len(sys.argv)

x =str(sys.argv[1])



if x =='--help':
    print('Do you need help?', x)
elif x == '--fast':
    print('fast mode enabled', x)
else:
    print('slow mode enabled', x)
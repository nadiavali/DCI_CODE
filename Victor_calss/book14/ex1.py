
from __future__ import print_function, division

import os


# def walk(dirname):
"""Prints the names of all files in dirname and its subdirectories.
    This is the version in the book.
    dirname: string name of directory
    """
    # for name in os.listdir(dirname):
    #     path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)


# def walk2(dirname):
#     """Prints the names of all files in dirname and its subdirectories.
#     This is the exercise solution, which uses os.walk.
#     dirname: string name of directory
#     """
#     for root, dirs, files in os.walk(dirname):
#         print('root', root)
#         print('dirs', dirs)
#         print('files',files)
#         for filename in files:
#             print(os.path.join(root, filename))


# if __name__ == '__main__':
#     walk('.')
#     walk2('.')

def sed(pattern, replacement,file, file2):
    
    #if os.path.isfile(file):
        f = open(file,'r')
        
        print(f)
        f2 = open(file2, 'a')
        for i in f:
            
            i =i.replace(pattern, replacement)
            f2.write(i)
            
        

sed('ok','am','n.txt','s.txt')
import os

def rm(file_name):
    os.remove(file_name)
    return f'{file_name}removed successfully'


if __name__ =='__main__':
    filename = input('what file you wanna delete?')
    rm(filename)
    
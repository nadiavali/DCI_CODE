x = int(input('num'))

if x>1:
    for i in range(2,x):
        if  x%i ==0 :
            print('not prime')
        
    else:
        print('prime')

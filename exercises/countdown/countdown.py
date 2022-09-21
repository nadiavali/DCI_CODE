from time import sleep
def countdown(t):
    for i in range(t,0,-1):
        sleep(1)
        print('Remaining Time: ', i)
t = int(input('Start the countdown from?! '))
countdown(t)
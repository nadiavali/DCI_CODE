print('You wanna cook! choose the cuisine type!')
print('1.Persian, 2.German 3.Italian')
choice = input('choose:')
if choice == '1':
    print('Congratulation! You made the best possible choice!')
    print('where is your current location?')
    loc = input('1.Iran, 2.Europe, 3.USA')
    if loc == '1':
        print('well you can have the access to all the ingredients, are you a vegetarian?')
        veg = input('1.yes, 2.No')
        if veg =='1':
            print('kookoo Sabzi, could be the best choice! google it you lazy human!!!')
        else:
            print('anyway there is vegetable in your food! you can not skip it you cheater!!!')
    elif loc == '2':
        print('First find some saffron! Do not cheat You can not use tumeric instead!!!')
    else:
        print('Currently your country is embargoed! communicate with your government!!! ')
elif choice == '2':
    print('Hmm, are you maybe Vegan or Vegetarian?!')
    vegM = input("1.Vegan, 2.Vegetarian,  3.No I don't use so much vegetables!" )
    if vegM == '1':
        print(' You better to leave the country ASAP!!!')
    elif vegM == '2':
        print('Hey dude! No chance! eat meat or die!')
    else:
        print('''Welcome to the land of meat!
         Here is the Holy Heaven for you! 
         But for your own sake eat some vegetables!''')
else:
    print('Ask Fausto!')
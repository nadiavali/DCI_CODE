
temp,tempCon = int(input('Please enter a temperature')), str(input('for Fahrenheit enter f, and for Celsius enter c'))
if tempCon == 'c' :
    print((temp*1.8)+32)
else:
    print((temp-32)/1.8)


from datetime import datetime, timedelta

# Task1

current_datetime =datetime.today()
print(current_datetime - timedelta(days=15))

# Task2

current_datetime =datetime.today()
print(current_datetime + timedelta(days=7))

# Task3

start_date = str(input('When is the start date of yor rent? (in DD-MM-YYYY)'))
name = input('what is your name?')
price = input ('How much you pay?')
convert_date =print(datetime.strftime(start_date,'%d-%B-%Y'))
print('Hey' + name + 'your rent of' + price + '€' + 'is due on' + convert_date )
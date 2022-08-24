#task1
city = 'London'
print(city)


#task2

city, population = 'berlin', '3645000'
print(city.capitalize(), ':', population)

#task3

city, population = 'london', '9000000'
print('City', ':', city.capitalize(), '(',(city.isalpha()),')')
print('Population',':', population)

#task4

text = '''Berlin is
surrounded by the State of
Brandenburg and contiguous with
Potsdam, Brandenburg's capital.'''

print('Capital', ':', text.index('capital'))

#task5

text = '''Berlin
straddles the banks of the
Spree, which flows into the
Havel (a tributary of the Elbe)
in the western borough of Spandau.'''
print(text.split())

#task6

text = '''Berlin is surrounded by the
State of Brandenburg and contiguous with
Potsdam, Brandenburg's capital.'''
print(text.replace('capital','capital of Germany'))
locations = { "Berlin" }
#Add to this set, two of your favorite cities. Use add and update


my_fav ={'Shiraz','Bushehr'}
locations.update(my_fav)
print(locations)

locations.add('Isfahan')
print(locations)
locations.pop()
print(locations)
locations.remove('Berlin')
print(locations)
locations.discard('Berlin')
locations.clear()
print(locations)
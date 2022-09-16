def summer():
    print("oh sunny day!")

​def winter():
    print("oh snowy day!")


print("# def summer -> ID")
print(id(summer))
print("# def winter -> ID")
print(id(winter))

print("\n# original summer:")
summer()
# function summer gets a new name (reference stays the same)
summer_link = summer

print("\n# original winter:")
winter()

# here the former function name summer gets a new function (reference) assigned to it
summer = winter 
print("\n# former summer, now winter")
print("# summer has now id of winter.")
# summer now executes the function of winter()
summer()
print("# id(summer)")
print(id(summer))

# function summer still exists, but with another name
print("\n# summer-link:")
summer_link()
print("# id(summer_link) still has the same id as original summer")
print(id(summer_link))
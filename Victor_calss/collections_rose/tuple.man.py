days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
hello =tuple('hello')
print(hello)
empty_tuple = tuple()
print(days[0:2])
print(days.index('Monday'))
print(days.count('Friday'))
#days[0] = 'sunday' #TypeError



days = (["Monday"], ["Tuesday"])
days[0][0] = "Sunday"
days[1].pop()
days[1].append("Monday")
print(days)
(['Sunday'], ['Monday'])
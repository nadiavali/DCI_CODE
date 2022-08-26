def Normalize(n):
    n.lower()
    n.capitalize()
    result = n.capitalize()+'!'
    return result

print(Normalize('TODAY IS A GREAT DAY'))
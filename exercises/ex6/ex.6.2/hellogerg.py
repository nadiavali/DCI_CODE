given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked.""" #Hello Gregor
def print_something():
    print(given_string.index('H'))
    print(given_string.index('e'))
    print(given_string.index('l'))
    print(given_string.index('o'))
print(given_string[124]+given_string[2]+given_string[46]+given_string[46]+given_string[5]+given_string[3]+given_string[18:25])

text = input('write about Nemo or Timo!')

a = text.find('Nemo')
if a:
   print('I found Nemo at' + str(a))
else:
    print("I can't find Nemo")
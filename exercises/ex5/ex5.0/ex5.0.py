def conCa(z):
  
    if  z[-1] == 'a' or z[-1] == 'e' or z[-1] =='i' or z[-1] =='u'or z[-1] =='o' :
     return z+'inator'+str(len(z))+'000'
     
    return z+'-inator'+str(len(z))+'000'

print(conCa('manamt'))
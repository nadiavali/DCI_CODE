def conCa(z):
  
    if  z[-1] == 'a':
     return z+'inator'+str(len(z))+'000'
     
    else:
        return z+'-inator'+str(len(z))+'000'

print(conCa('manam'))
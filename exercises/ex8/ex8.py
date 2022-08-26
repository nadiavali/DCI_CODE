def finding_Nemo(text):
   if text.find('Nemo') != -1:
      result = 'I found Nemo at' + str(text.find('Nemo'))
   else:
      result = "I can't find Nemo :("
   return result
print(finding_Nemo('I am Nemo'))
print(finding_Nemo('I am Nadia'))
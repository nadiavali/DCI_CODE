from datetime import datetime


user = str(input('your birthday! '))

birthday = datetime.strptime(user,'%d-%m-%Y')
convert_birthday = birthday.strftime('%Y,%B,%d')

now = datetime.now()
print('Your Birthday is on :', convert_birthday)
since = now - birthday
sinceDays = since.days

sinceY= sinceDays//365
SinceR = sinceDays % 365

sinceW = SinceR // 7

sinceRR = sinceW % 7
print('years:',sinceY, 'weeks:', sinceW, 'days:', sinceRR)
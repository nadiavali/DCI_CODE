
from datetime import datetime

class Employee():
    
    num_of_emp = 0
    raise_amount = 1.04  #atribute

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp = Employee.num_of_emp + 1 # not self because we dont wanna make instances of it

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # thi is method
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):  # raise the raise_amount =1.o6 
        cls.raise_amount = amount
#print(Employee.raise_amount)
#print(Employee_1.raise_amount)

    @classmethod
    def from_string(cls, emp_str): #using class method as alternative constructor
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day): # take no instance and no class as the argument
        if day.weekday() == 5 or day.weekday() ==6: # 6 sunday 5 saturday which are not work day
            return False
        return True

Employee_1 = Employee('Corey', 'Schafer', 50000)
Employee_2 = Employee('Nadia', 'vali', 60000)

from datetime import datetime, date
my_date = datetime(2022, 7, 10) # is sunday and off day so False


print(Employee.is_work_day(my_date))

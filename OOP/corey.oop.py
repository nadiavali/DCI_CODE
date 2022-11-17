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

print(Employee.num_of_emp) # compare with l 26

Employee_1 = Employee('Corey', 'Schafer', 50000)
Employee_2 = Employee('Nadia', 'vali', 60000)


emt_string1 = 'John-Doe-80000'

new_em_1 = Employee.from_string(emt_string1)
print(new_em_1.email)
print(new_em_1.pay)
print(Employee.num_of_emp) # 2 instances only we have


Employee.set_raise_amt(1.06)

print(Employee.raise_amount)
print(Employee_1.raise_amount)


# Employee.fullname(Employee_1)
# #print(Employee.raise_amount)
# # print(Employee_1.raise_amount)
# # print(Employee_1.apply_raise())
# print(Employee_1.pay)

# print(Employee_1.__dict__)
# # print(Employee.__dict__)

# Employee_1.raise_amount = 1.05

# print(Employee_1.__dict__)  #important
# print(Employee.raise_amount)
# print(Employee_1.raise_amount)
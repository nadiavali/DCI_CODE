
# Managers: They walk around yelling at people telling them what to do. They are salaried employees and
#  make more money.

# Secretaries: They do all the paper work for managers and ensure that everything gets billed and
#  payed on time. They are also salaried employees but make less money.

# Sales employees: They make a lot of phone calls to sell products. They have a salary, but they also
#  get commissions for sales.

# Factory workers: They manufacture the products for the company. They are paid by the hour.

import hr

class Manager(hr.SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')
        

class Secretary(hr.SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(hr.CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(hr.HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
import hr
import employees
import productivity


# salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([salary_employee, hourly_employee,commission_employee])


# salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])

# import hr
# import disgruntled

# salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee,
#     disgruntled_employee
# ])


manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)


# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)
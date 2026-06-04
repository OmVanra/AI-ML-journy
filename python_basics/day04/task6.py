# Q6. Create an abstract class 
# Employee with an abstract method
# calculate_salary(). 
# Create subclasses , 
# Intern ,FullTimeEmployee , and 
# ContractEmployee that
# implement the method differently.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class FullTimeEmployee(Employee):
    def __init__(self, annual_slary):
        self.annual_slary = annual_slary
    def calculate_salary(self):
        return self.annual_slary / 12
class ContractEmployee(Employee):
    def __init__(self, contract_amount):
        self.contract_amount = contract_amount
    def calculate_salary(self):
        return self.contract_amount
# Example usage
intern = Intern(15, 160)
full_time_employee = FullTimeEmployee(60000)
contract_employee = ContractEmployee(5000)
print(f"Intern Salary: {intern.calculate_salary()}")
print(f"Full Time Employee Salary: {full_time_employee.calculate_salary()}")
print(f"Contract Employee Salary: {contract_employee.calculate_salary()}")


class Employee:
    def __init__(self, name, position, salaries):
        self.name = name
        self.position = position
        self.salaries = salaries

    def annual_salary(self):
        return sum(self.salaries)

    def salaries_greater_than(self, amount):
        return [s for s in self.salaries if s > amount]

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Annual Salary: {self.annual_salary()}"


class Manager(Employee):
    def __init__(self, name, position, salaries, department):
        super().__init__(name, position, salaries)
        self.department = department

    def __str__(self):
        return super().__str__() + f", Department: {self.department}"


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.annual_salary() for emp in self.employees)
        return total_salary / len(self.employees)

    def highest_paid_employee(self):
        if not self.employees:
            return None
        return max(self.employees, key=lambda emp: emp.annual_salary())


# --- Приклад використання ---
emp1 = Employee("Олена", "Програміст", [1200, 1300, 1250, 1400])
emp2 = Employee("Ігор", "Дизайнер", [1100, 1150, 1130, 1170])
mgr1 = Manager("Світлана", "Менеджер проектів", [2000, 2100, 2050, 2150], "Розробка")

print(emp1)
print(emp2)
print(mgr1)

print("\nЗарплати Олени більше 1250:", emp1.salaries_greater_than(1250))

company = Company("Tech Solutions")
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(mgr1)

print("\nСередня зарплата в компанії:", company.average_salary())
print("Найбільш оплачуваний працівник:", company.highest_paid_employee())

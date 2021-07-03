# class Employee:
#     company = "Bharat Gas"
#     salary = 5600
#     salarybonus = 400
#     # totalSalary = 6100

#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus

#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salarybonus = val - self.salary

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 5800
# print(e.salary)
# print(e.salarybonus)


class Employe:
    company="Bharat gas"
    salary=5600
    salarybonus=500
    totalsalary=6100

    @property
    def totalsalary(self):
       return self.salary + self.salarybonus
e=Employe()
print(e.totalsalary)
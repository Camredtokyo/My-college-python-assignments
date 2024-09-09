# Write a program to create a dictionary by combining two lists ‘ name’ for employee name and ‘salary’ for employee 
# salary. Use the list ‘name’ as the key and ‘salary’ as the value of dictionary elements.

names = []
salaries = []

num_employees = int(input("Enter the number of employees: "))
i = 0
while i < num_employees:
    name = input(f"Enter the name of employee {i + 1}: ")
    names.append(name)
    i = i + 1

i = 0
while i < num_employees:
    salary = int(input(f"Enter the salary of employee {i + 1}: "))
    salaries.append(salary)
    i = i + 1

employee_dict = {}

i = 0
while i < num_employees:
    employee_dict[names[i]] = salaries[i]
    i = i + 1

print(employee_dict)
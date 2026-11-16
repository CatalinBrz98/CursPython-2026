from big_project.classes.employees import Employee
from db.db import read_from_db

def read_employee_data(file_path):
    employee_data = read_from_db(file_path)
    processed_employee_data = []
    for employee in employee_data:
        processed_employee_data.append(Employee(employee["firstname"], employee["surname"], employee["salary"]))

    return processed_employee_data


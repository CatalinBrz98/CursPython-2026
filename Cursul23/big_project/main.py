from classes import Employee, Manager
from dependencies import read_employee_data

if __name__ == "__main__":
    employee1 = Employee("Ionut", "Mihai", 4000)
    employee2 = Employee("Mihai", "Ionut", 5000)
    manager1 = Manager("Alexandru", "Mihaita", 7000, [employee1, employee2])
    print(manager1)

    emplyee_data = read_employee_data("dependencies/db/db.csv")
    print(emplyee_data)

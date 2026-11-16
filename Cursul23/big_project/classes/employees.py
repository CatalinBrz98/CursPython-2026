class Employee:
    def __init__(self, firstname: str, surname: str, salary: float):
        self.firstname = firstname
        self.surname = surname
        self.salary = salary

    @property
    def fullname(self):
        return f'{self.firstname} {self.surname}'

    def __str__(self):
        return f'Emplyoee({self.fullname}, {self.salary})'


class Manager(Employee):
    def __init__(self, firstname: str, surname: str, salary: float, employees: list[Employee]):
        super().__init__(firstname, surname, salary)
        self.employees = employees

    def __str__(self):
        return f'Manager({self.fullname}, {self.salary}, {len(self.employees)})'

class Person:
    def __init__(self, per_fname, per_lname, per_age):
        self.fname = per_fname
        self.lname = per_lname
        self.age = per_age

    def get_full_name(self):
        print("name", self.fname + " " + self.lname)

    def get_age(self):
        print("age:", self.age)


class Employee(Person):
    def __init__(self, emp_fname, emp_lname, emp_age, emp_salary):
        self.salary = emp_salary
        super().__init__(emp_fname, emp_lname, emp_age)

    def get_emp_info(self):
        super().get_full_name()
        super().get_age()
        print("salary", self.salary)

    def update_salary(self, new_salary):
        self.salary = new_salary


emp = Employee("john", "smith", 20, 8000)

emp.get_emp_info()

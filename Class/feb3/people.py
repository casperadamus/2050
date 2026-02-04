class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def get_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return "Your name is " + self.first_name + " " + self.last_name


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grad_year = year
    
    def get_year(self):
        return self.grad_year



if __name__ == "__main__":
    per1 = Person("John", "Smith")
    print(per1)
    per1.get_name()

    per2 = Student("Ava", "Smith", 2022)
    print(per2)
    per2.get_name()
    print(per2.get_year())


import unittest  # very powerful testing module
from people import Person, Student  # classes to be tested


class TestPerson(unittest.TestCase):
    # Create one test_* method per attribute to test
    def test_init(self):
        p1 = Person('John', 'Smith')
        self.assertEqual(p1.first_name, 'John')
        self.assertEqual(p1.last_name, 'Smith')
    
    def test_get_name(self):
        p2 = Person('John', 'Smith')
        self.assertEqual(p2.get_name(), "John Smith")
    
    def test_str(self):
        p2 = Person('John', 'Smith')
        self.assertEqual(str(p2), "Your name is John Smith")


class TestStudent(unittest.TestCase):
    # Create one test_* method per attribute to test
    def test_init(self):
        p1 = Student('John', 'Smith', 2022)
        self.assertEqual(p1.first_name, "John")
        self.assertEqual(p1.last_name, "Smith")
        self.assertEqual(p1.grad_year, 2022)
    
    def test_get_year(self):
        p1 = Student('John', 'Smith', 2022)
        self.assertEqual(p1.get_year(), 2022)


# run all "test_*" methods in all "Test*" classes above
unittest.main()

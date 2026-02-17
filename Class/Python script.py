class Student:
    """A student with grades that must be in valid range"""
    
    def __init__(self, name, student_id):
        """
        Create a new student.
        
        Args:
            name (str): Student's name
            student_id (str): Student ID (must be 6 digits)
        
        Raises:
            ValueError: If student_id is not 6 digits
        """
        if not student_id.isdigit() or len(student_id) != 6:
            raise ValueError(f"Student ID must be exactly 6 digits. Got: '{student_id}'")
        
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """
        Add a grade for the student.
        
        Args:
            grade (float): Grade value (must be between 0 and 100)
        
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        if not 0 <= grade <= 100:
            raise ValueError(f"Grade must be between 0 and 100. Got: {grade}")
        
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")
    
    def get_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """Get letter grade based on average"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        avg = self.get_average()
        letter = self.get_letter_grade()
        return (f"Student(name='{self.name}', id={self.student_id}, "
                f"average={avg:.2f}, grade={letter})")


# Demonstrating the Student class
print("\n--- Creating students ---")

# Valid student creation
student1 = Student("Alice Smith", "123456")
print(f"Created: {student1}")

# Invalid student creation (wrong ID length)
print("\nTrying to create student with short ID:")
try:
    student2 = Student("Bob Jones", "123")
except ValueError as e:
    print(f"❌ ValueError: {e}")

# Invalid student creation (non-numeric ID)
print("\nTrying to create student with non-numeric ID:")
try:
    student3 = Student("Charlie Brown", "ABC123")
except ValueError as e:
    print(f"❌ ValueError: {e}")

print("\n--- Adding grades ---")

# Valid grades
student1.add_grade(95)
student1.add_grade(87)
student1.add_grade(92)

# Invalid grade (too high)
print("\nTrying to add grade over 100:")
try:
    student1.add_grade(105)
except ValueError as e:
    print(f"❌ ValueError: {e}")

# Invalid grade (negative)
print("\nTrying to add negative grade:")
try:
    student1.add_grade(-10)
except ValueError as e:
    print(f"❌ ValueError: {e}")

print(f"\nFinal student state: {student1}")


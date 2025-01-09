# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cpi = None
        print(f"Student {self.name} created.")

    def display(self):
        """Displays the name and age of the student."""
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        """Destructor to indicate when the object is deleted."""
        print(f"Destructor called. Student {self.name} object deleted.")

    def calculate_cpi(self, grades):
        """
        Calculates the CPI (Cumulative Performance Index) 
        based on a list of grades provided.
        """
        if not grades:
            raise ValueError("Grades list cannot be empty.")
        self.cpi = sum(grades) / len(grades)

    def display_cpi(self):
        """Displays the CPI if it has been calculated."""
        if hasattr(self, 'CPI'):
            print("CPI:", self.cpi)
        else:
            print("CPI has not been calculated yet.")

    def is_eligible_for_scholarship(self, min_cpi=8.0):
        """
        Checks if the student is eligible for a scholarship
        based on a minimum CPI requirement.
        """
        if not hasattr(self, 'cpi'):
            print("CPI has not been calculated yet. Cannot determine eligibility.")
            return False
        return self.cpi >= min_cpi

    def grade_performance(self):
        """
        Grades the student's performance based on their CPI.
        """
        if not hasattr(self, 'cpi'):
            print("CPI has not been calculated yet.")
            return None
        if self.cpi >= 9.0:
            return "Excellent"
        elif self.cpi >= 8.0:
            return "Very Good"
        elif self.cpi >= 7.0:
            return "Good"
        elif self.cpi >= 5.0:
            return "Average"
        else:
            return "Below Average"


# Example usage of the Student class

# Create a student object
student1 = Student("Alice", 20)

# Display student details
student1.display()

# Calculate and display CPI
grades = [8.0, 9.0, 7.0, 8.0, 10.0, 11.0, 6.0]
student1.calculate_cpi(grades)
student1.display_cpi()

# Check scholarship eligibility
if student1.is_eligible_for_scholarship():
    print(f"{student1.name} is eligible for a scholarship!")
else:
    print(f"{student1.name} is not eligible for a scholarship.")

# Display performance grade
print("Performance Grade:", student1.grade_performance())

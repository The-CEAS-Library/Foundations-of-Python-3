# Fuction to get the first anme, last name and year of birth of a person
def demographics():
    first_name = input('What is your First Name: ')
    last_name = input('What is your Last Name: ')
    year_of_birth = input('What is your Year of Birth: ')
    return [first_name, last_name, year_of_birth]

# Fuction to return he six plus two    
def uc_6_2(first_name, last_name):
    if (len(last_name)>=6):
        sixplus2 = last_name[0:6] + first_name[0] + first_name[-1]
    else:
        sixplus2 = last_name + first_name[0:(6-len(last_name)+1)] + first_name[-1]
    return(sixplus2.lower())

# Student class definition
class Student:
    student_count = 0
    # initialisation method
    def __init__(self, first_name, last_name, year_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        Student.student_count = Student.student_count + 1
        self.num = Student.student_count # Save for creation of student number
    # Method to return student number (year of birth + count)
    def student_number(self):
        return self.year_of_birth + str(self.num)
    # Metod to return student UC six plus two
    def student_id(self):
        return uc_6_2(self.first_name, self.last_name)

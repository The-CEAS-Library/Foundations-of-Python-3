# Fuction to get the first name, last name and year of birth of a person
def demographics():
    first_name = '' # Replace this line with the right code to take input for user's first name
    
    last_name = '' # Replace this line with the right code to take input for user's last name
    
    year_of_birth = '' # Replace this line with the right code to take input for user's year of birth
    
    return '', '', '' # Replace this line with the right code to return first name, last name and year of birth in that order




# Fuction to return the six plus two
# You may copy and paste the uc_6_2 function defined earlier     
def uc_6_2(first_name,last_name):
    # Use the appropriate If and else Decision Block with a condition that compares the Length of the Last name
    # In the If and else Decision Block store the six plus two in a variable
    # Use the Tips below in your If and else Decision Block
    if len(last_name) >= 6:
        six_plus_2 = '' # Replace this line with the right code
        
    # Continue the "If..elif..else" block with the appropriate block for the remaining scenario
    
    # Return the six plus two in lower case
    return

# Tips (Replace the portions marked as with ?)
# ********************************************
# For length of the last name is >=6, sixplus2 = last_name[0:?] + first_name[0] + first_name[?]
# For length of the last name is <6, sixplus2 = last_name + first_name[0:(6-len(?)+1)] + first_name[?]




# Student class definition
class Student:
    # Start the student population count at 0
    student_count = 0
    # initialisation method
    def __init__(self,par_first_name): # Add all the necessary class parameters
        self.var_first_name = par_first_name # Setting the Instance variable for the first name
        # Follow the example above to initialize all other Instance variables
        
        
        # Correct command below to increment the class parameter for student population by 1
        Student.student_count = Student.student_count + 0
        
        # Setting an Instance variable for the current student number to the current student coun
        self.num = Student.student_count # Save for creation of student number
        
    # Method to return student number (year of birth + count)
    def student_number(self):
        # Use the hint below to return the student's yeaar of birth + student's number
        return
        
        # Hint: return self.year_of_birth + '?'
        # Correct the code above by repacing '?'
        # Student's number is a number so you may have to use the str() function to convert to string
        # to make concatenation possible




    # Metod to return student UC six plus two
    def student_id(self):
        # Call apprrioprate fuction above to return the UC 6+2
        return

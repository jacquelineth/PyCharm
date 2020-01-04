students = []


class Student: 
    #Clas Attribute
    school_name= "Springfield Elementary"

    # Constructor
    ### Need __init__  and self parameter
    def __init__(self, name, student_id =332) :
        self.name=name
        self.student_id=student_id
        students.append(self)
        
    
    # Public Attribut
    # name = ""

    def __str__(self):
        return " Student :( " + self.name + " )"


    def get_name_capitalize(self) :
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

mark = Student("mark")

# SubClass
class HighSchoolStudent(Student):
    
    school_name = "Springfield High Scool"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())
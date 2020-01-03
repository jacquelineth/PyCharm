students = []


class Student: 
    # Constructor
    ### Need __init__  and self parameter
    def __init__(self, name, student_id =332) :
        xstudent = {"name": name, "student_id": student_id}
        students.append(xstudent)
        self.sName=name
        self.__HName__= "private"
    
    # Public Attribut
    sName = ""

    # private Attribut
    __HName__ = ""

    def __str__(self):
        return super().__str__() + " Student :( " + self.sName + " )"

student = Student("Mark")


print(student)
print(student.__HName__)

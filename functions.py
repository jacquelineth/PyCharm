students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


#default arg
def add_student(name, student_id =332) :
    student = {"name": name, "student_id": student_id}
    students.append(student)


# varg Functions with *named *Variable Argument Lists
def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"] ,kwargs["pluralsight_Susbsccirber"] )


student_list = get_students_titlecase()

add_student("Mark")
var_args("Mark", description="Love Python ", feedback= None, pluralsight_Susbsccirber= True)
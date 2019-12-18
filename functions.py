students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase.append( student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


#default arg
def add_student(name, student_id =332) :
    xstudent = {"name": name, "student_id": student_id}
    students.append(xstudent)


student_list = get_students_titlecase()
end = False 
res = True

while res:
    resChar= input("Add Student( y/n) ?" )
    if resChar == "y" or resChar == "y":
        student_name = input("Enter student name: " )
        student_id = input("Enter student ID: " )
        add_student(student_name, student_id)
    else:
        res= False



print_students_titlecase()
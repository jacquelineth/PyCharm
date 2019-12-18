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
    save_file(xstudent)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student["name"]+"\n")
        f.flush()
        f.close()
    except Exception:
        print("Could not save file")



def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

student_list = get_students_titlecase()


read_file()
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
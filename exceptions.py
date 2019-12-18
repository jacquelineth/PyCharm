student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
try:
    last_name= student["last_name"] 
except KeyError:
    print("Error findng last_name")
       
print("Finished")
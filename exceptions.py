student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name= student["last_name"] 
    numbered_last_name= 3 + last_name
except KeyError:
    print("Error findng last_name")
except  TypeError as error:
    print("I can't add these 2 together")
    print(error)
except Exception:
    print("Un")


print("Finished")
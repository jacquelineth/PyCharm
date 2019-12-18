student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["name"] =="Mark"
# retrieve non existing key with defaultvalue
student.get("last_name", "Unknown") == "Unknown"

# retrieve  all
student.keys() == ["name", "student_id", "feedback"]
student.values() == ["Mark", 15163, None]

#changing value
student["name"] = "James"
#deleting value
del student["name"]
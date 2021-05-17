friend_ages = {"Rolf": 24, "Adam": 30, "Jamie": 19} 

friend_ages["Rolf"] = 20

print(friend_ages)

#List of dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

print(friends[1]["name"])

#Attendance dictionary
student_attendance = {"Rolf": 24, "Adam": 30, "Jamie": 19}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
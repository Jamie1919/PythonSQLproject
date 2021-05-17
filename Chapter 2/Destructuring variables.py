t = 5, 11
x, y = t

print(x, y)

#Attendance dictionary
student_attendance = {"Rolf": 24, "Adam": 30, "Jamie": 19}

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)
    #print(f"{student}: {attendance}")

#Example tuple
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

#Head or tail
*head, tail= [1, 2, 3, 4, 5]
print(*head)
print(tail)
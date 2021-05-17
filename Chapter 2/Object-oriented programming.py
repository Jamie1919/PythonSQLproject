student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


    print(average(student['grades']))



#Sytax
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (89, 90, 93, 78, 90))
student2 = Student("Rolf", (100, 60, 93, 89, 90))

print(student.average_grades())
print(student.average_grades(student2))


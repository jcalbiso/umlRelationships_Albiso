class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, students):
        self.students = students

student1 = Student("Jacob")
student2 = Student("Alex")

classroom = Classroom([student1, student2])

print(classroom.students[0].name)
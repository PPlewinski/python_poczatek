#
# class Student:
#     def __init__(self):
#         print("powstaje nowy obiekt")
#
# if __name__ == "__main__":
#     student = Student()

# class Student():
#     def __init__(self):
#         self.first_name = "Paweł"
#         self.last_name = "Plewiński"
#         self.age = 18
#
# def run_example():
#     student = Student()
#     # print(student.first_name)
#     # print(student.last_name)
#     # print(student.age)
#     student.first_name = "Michał"
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
#
# if __name__ == '__main__':
#     run_example()


import random
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students







class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False



def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student in range(number_of_students):
        first_name = f"Student {student}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))
    school = School(school_name, students)
    return school


def run_example():
    school = create_school_with_students("Hogwart's")
    print(school)
    for student in school.students:
        print(student.first_name, student.last_name, student.promoted)

# def promote_student(student):
#     student.promoted = True

if __name__ == "__main__":
    run_example()

class TooManyStudents(Exception):
    pass

class Classroom:
    def __init__(self, teacher, course_title, students):
        self.teacher = teacher
        self.course_title = course_title
        self.students = students

    def add_student(self, student):
        if len(self.students) < 20:
            self.students.append(student)
        else:
            raise TooManyStudents("Cannot add more than 20 students")


    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break


    def change_teacher(self, new_teacher):
        self.teacher = new_teacher



class Person():
    def __init__(self, name, age):
        self.name = name


class Teacher(Person):
    pass


class Student(Person):
    pass

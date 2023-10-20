class Student:
    def __init__(self, name, surname, age, average_point):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_point = average_point
class Students:
    def __init__(self, file_data):
        self.file_data = file_data
        self.student_list = []
    
    def add_student(self, name, surname, age, average_point):
        student = Student(name, surname, age, average_point)
        self.student_list.append(student)
        with open(self.file_data, 'a') as file:
            file.write(f'{name} {surname} {age} {average_point}\n')
    def delete_student(self, name, surname):
        self.student_list = [student for student in self.student_list if student.name != name or student.surname != surname]
        with open(self.file_data, 'w') as file:
            for student in self.student_list:
                file.write(f'{student.name} {student.surname} {student.age} {student.average_point}\n')
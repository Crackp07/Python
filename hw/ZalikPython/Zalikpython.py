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
    def change_inf_student(self, name, surname, newinfo):
        for student in self.student_list:
            if student.name == name and student.surname == surname:
                student_info = newinfo.split()
                student.name = student_info[0]
                student.surname = student_info[1]
                student.age = student_info[2]
                student.average_point = student_info[3]
        with open(self.file_name, 'w') as file:
            for student in self.student_list:
                file.write(f'{student.name} {student.surname} {student.age} {student.average_point}\n')
    def display_studen(self):
        for student in self.student_list:
            print(f'{student.name} {student.surname} {student.age} {student.average_point}')
    def search_student(self, search_value, value):
        for student in self.student_list:
            if search_value == 'name' and value in student.name:
                print(f'{student.name} {student.surname} {student.age} {student.average_point}')
            elif search_value == 'name' and value in student.surname:
                print(f'{student.name} {student.surname} {student.age} {student.average_point}')
    def display_exellent(self):
        for student in self.student_list:
            if float(student.average_point) >= 10:
                print(f'{student.name} {student.surname} {student.age} {student.average_point}')
    def display_student_in_order(self):
        self.student_list.sort(key=lambda student: (student.surname, student.name))
        for student in self.student_list:
            print(f'{student.name} {student.surname} {student.age} {student.average_point}')
file_name = 'students.txt'
students = Students(file_name)
while True:
    print('1. Додати студента')
    print('2. Видалити студента')
    print('3. Змінити інформацію про студента')
    print('4. Показати на екрані ВСІХ студентів')
    print('5. Вивести на екран інформацію про студента за параметром')
    print('6. Вивести студентів в певному порядку')
    print('7. Вивести "відмінників"')
    print('8. Вийти')
    choice = input('Виберіть опцію (1/2/3/4/5/6/7/8): ')
    if choice == '1':
        name = input('Введіть ім\'я студента: ')
        surname = input('Введіть прізвище студента: ')
        age = input('Введіть вік студента: ')
        average_point = input('Введіть середній бал студента: ')
        students.add_student(name, surname, age, average_point)
    elif choice == '2':
        name = input('Введіть ім\'я студента, якого потрібно видалити: ')
        surname = input('Введіть прізвище студента, якого потрібно видалити: ')
        students.delete_student(name, surname)
    elif choice == '3':
        name = input("Введіть ім'я студента: ")
        surname = input('Введіть прізвище студента: ')
        newinfo = input('Введіть нову інформацію про студента: ')
        students.change_inf_student(name, surname, newinfo)
    elif choice == '4':
        students.display_studen()
    elif choice == '5':
        search_value = input("Введіть параметр пошуку (ім'я, прізвище тощо): ")
        value = input('Введіть значення для пошуку: ')
        students.search_student(search_value, value)
    elif choice == '6':
        students.display_student_in_order()
    elif choice == '7':
        students.display_exellent()
    elif choice == '8':
        break
    else:
        print('Неправильний вибір. Спробуйте ще раз.')






import os

class Student:
    def __init__(self, student_id, first_name, last_name, average_grade):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.average_grade = average_grade

    def to_string(self):
        return f"ID: {self.student_id}, Повне і'мя: {self.first_name} {self.last_name}, Середній бал: {self.average_grade}"

class StudentManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_file(self):
        with open(self.file_name, 'w') as file:
            pass

    def add_student(self, student):
        with open(self.file_name, 'a') as file:
            file.write(f"{student.student_id},{student.first_name},{student.last_name},{student.average_grade}\n")

    def delete_student(self, student_id):
        students = self.load_students()
        updated_students = [student for student in students if student.student_id != student_id]
        with open(self.file_name, 'w') as file:
            for student in updated_students:
                file.write(f"{student.student_id},{student.first_name},{student.last_name},{student.average_grade}\n")

    def update_student(self, student_id, new_data):
        students = self.load_students()
        for student in students:
            if student.student_id == student_id:
                student.first_name = new_data.get('first_name', student.first_name)
                student.last_name = new_data.get('last_name', student.last_name)
                student.average_grade = new_data.get('average_grade', student.average_grade)
                break

        with open(self.file_name, 'w') as file:
            for student in students:
                file.write(f"{student.student_id},{student.first_name},{student.last_name},{student.average_grade}\n")

    def load_students(self):
        students = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        student = Student(parts[0], parts[1], parts[2], float(parts[3]))
                        students.append(student)
        except FileNotFoundError:
            self.create_file()
        return students

    def show_all_students(self):
        students = self.load_students()
        for student in students:
            print(student.to_string())

    def search_students(self, search_param, value):
        students = self.load_students()
        found_students = []

        for student in students:
            if search_param == "ID" and student.student_id == value:
                found_students.append(student)
            elif search_param == "ім'я" and student.first_name == value:
                found_students.append(student)
            elif search_param == "прізвище" and student.last_name == value:
                found_students.append(student)

        if found_students:
            for student in found_students:
                print(student.to_string())
        else:
            print("Студентів із зазначеними критеріями не знайдено.")

    def sort_students(self, order_by):
        students = self.load_students()

        if order_by == "алфавітний порядок":
            students.sort(key=lambda x: (x.last_name, x.first_name))
        elif order_by == "середній бал":
            students.sort(key=lambda x: x.average_grade, reverse=True)

        for student in students:
            print(student.to_string())

    def excellent_students(self):
        students = self.load_students()
        excellent_students = [student for student in students if student.average_grade >= 10]
        if excellent_students:
            for student in excellent_students:
                print(student.to_string())
        else:
            print("Відмінників не знайдено.")

if __name__ == "__main__":
    file_name = "students.txt"
    manager = StudentManager(file_name)

    while True:
        print("\nЗробіть вибір:")
        print("1. Створити або видалити файл")
        print("2. Додати студента")
        print("3. Видалити студента")
        print("4. Змінити інформацію про студента")
        print("5. Показати всіх студентів")
        print("6. Вивести на екран інформацію про студента за параметром")
        print("7. Вивести студентів в певному порядку")
        print("8. Вивести 'відмінників'")
        print("9. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            if os.path.exists(file_name):
                os.remove(file_name)
            manager.create_file()
            print(f"'{file_name}' було створено.")
        elif choice == "2":
            student_id = input("Введіть студентський ID: ")
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            average_grade = float(input("Введіть середню оцінку: "))
            student = Student(student_id, first_name, last_name, average_grade)
            manager.add_student(student)
        elif choice == "3":
            student_id = input("Введіть ID студента для видалення: ")
            manager.delete_student(student_id)
        elif choice == "4":
            student_id = input("Введіть ID студента для оновлення: ")
            first_name = input("Введіть ім'я (залиште порожнім, щоб зберегти актуальність): ")
            last_name = input("Введіть прізвище (залиште порожнім, щоб зберегти поточне): ")
            average_grade = input("Введіть середню оцінку (залиште порожнім, щоб зберегти поточний): ")
            new_data = {}
            if first_name:
                new_data['first_name'] = first_name
            if last_name:
                new_data['last_name'] = last_name
            if average_grade:
                new_data['average_grade'] = float(average_grade)
            manager.update_student(student_id, new_data)
        elif choice == "5":
            manager.show_all_students()
        elif choice == "6":
            search_param = input("Введіть параметр пошуку (ID, ім'я, прізвище): ")
            value = input(f"Введіть {search_param} для пошуку інформації: ")
            manager.search_students(search_param, value)
        elif choice == "7":
            order_by = input("Сортувати студентів за (алфавітний порядок, середній бал): ")
            manager.sort_students(order_by)
        elif choice == "8":
            manager.excellent_students()
        elif choice == "9":
            break
# # 1
# class Human:
#     count = 0 
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         Human.count += 1
#     def display(self):
#         print(f"Firstname: {self.firstname},Lastname: {self.lastname},  Age: {self.age}")
#     @staticmethod
#     def get_count():
#         return Human.count
# pers1 = Human("John","Black", 30)
# pers2 = Human("Linda","Brown", 29)
# pers3 = Human("Jim", "White", 31)
# print(f"Кількість створених об'єктів: {Human.get_count()}")
# # 2
# class CalculatorArea:
#     count = 0
#     @staticmethod
#     def area_triangle(base, height):
#         CalculatorArea.count += 1 
#         return (0.5 * base * height)
#     @staticmethod
#     def area_rectangle(lenght, width):
#         CalculatorArea.count += 1
#         return (lenght * width)
#     @staticmethod
#     def area_square(side):
#         CalculatorArea.count += 1
#         return (side ** 2)
#     @staticmethod
#     def area_rhombus(diagonal1, diagonal2):
#         CalculatorArea.count += 1
#         return (0.5 * diagonal1 * diagonal2)
#     @staticmethod
#     def get_calculator_count():
#         return CalculatorArea.count
# triangle_area = CalculatorArea.area_triangle(3,5)
# rectangle_area = CalculatorArea.area_rectangle(4,6)
# square_area = CalculatorArea.area_square(5)
# rhombus_area = CalculatorArea.area_rhombus(2,5)
# print(f"Площа трикутника: {triangle_area}")
# print(f"Площа прямокутника: {rectangle_area}")
# print(f"Площа квадрата: {square_area}")
# print(f"Площа ромба: {rhombus_area}")
# print(f"Кількість обчислень площі:{CalculatorArea.get_calculator_count()}")
# # 3
# class Calculator:
#     @staticmethod
#     def find_max(a,b,c,d):
#         return max(a,b,c,d)
#     @staticmethod
#     def find_min(a,b,c,d):
#         return min(a,b,c,d)
#     @staticmethod
#     def find_average(a,b,c,d):
#         return(a+b+c+d)/4
#     @staticmethod
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * Calculator.factorial(n-1)
# a,b,c,d = 5,10,3,8
# max_value = Calculator.find_max(a,b,c,d)
# min_value = Calculator.find_min(a,b,c,d)
# average_value = Calculator.find_average(a,b,c,d)
# factorial_value = Calculator.factorial(4)
# print(f"Максимум: {max_value}")
# print(f"Мінімум: {min_value}")
# print(f"Середнє арифметичне: {average_value}")
# print(f"Факторіал 4: {factorial_value}")
# # 4
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Мене звуть {self.name} і мені {self.age} років.")
# class Builder(Human):
#     def __init__(self, name, age, speciality):
#         super().__init__(name, age)
#         self.speciality = speciality
#     def build(self):
#         print(f"{self.name} - це робітник із спеціальністю '{self.speciality}'.")
# class Sailor(Human):
#     def __init__(self, name, age, ship_name):
#         super().__init__(name, age)
#         self.ship_name = ship_name
#     def sail()
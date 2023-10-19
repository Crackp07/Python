# # 1. Создайте класс Circle (окружность). Для данного 
# # класса реализуйте ряд перегруженных операторов:
# # - Проверка на равенство радиусов двух окружностей 
# # (операция = =);
# # - Сравнения длин двух окружностей (операции >, <, <=,>=);
# # - Пропорциональное изменение размеров окружности, 
# # путем изменения ее радиуса (операции + - += -=).
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __gt__(self, other):
#         return self.radius > other.radius

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __ge__(self, other):
#         return self.radius >= other.radius

#     def __le__(self, other):
#         return self.radius <= other.radius

#     def __add__(self, other):
#         return Circle(self.radius + other.radius)

#     def __sub__(self, other):
#         return Circle(self.radius - other.radius)

#     def __iadd__(self, other):
#         self.radius += other.radius
#         return self

#     def __isub__(self, other):
#         self.radius -= other.radius
#         return self

#     def __str__(self):
#         return f"Circle with radius {self.radius}"
# circle1 = Circle(5)
# circle2 = Circle(3)
# circle3 = Circle(5)
# print(circle1 == circle2)
# print(circle1 > circle2)
# print(circle1 < circle2)
# print(circle1 >= circle2)
# print(circle1 <= circle2)
# circle4 = circle1 + circle2
# circle5 = circle1 - circle2
# print(circle4)
# print(circle5)
# circle1 += circle2
# circle1 -= circle3
# print(circle1)

# # 2. Создайте класс Complex (комплексное число).
# # Создайте перегруженные операторы для реализации 
# # арифметических операций для по работе с комплексными 
# # числами (операции +, -, *, /).
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         real_part = self.real + other.real
#         imag_part = self.imag + other.imag
#         return Complex(real_part, imag_part)

#     def __sub__(self, other):
#         real_part = self.real - other.real
#         imag_part = self.imag - other.imag
#         return Complex(real_part, imag_part)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return Complex(real_part, imag_part)

#     def __truediv__(self, other):
#         denominator = other.real**2 + other.imag**2
#         real_part = (self.real * other.real + self.imag * other.imag) / denominator
#         imag_part = (self.imag * other.real - self.real * other.imag) / denominator
#         return Complex(real_part, imag_part)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"
# c1 = Complex(3, 4)
# c2 = Complex(2, -1)

# result_add = c1 + c2
# result_sub = c1 - c2
# result_mul = c1 * c2
# result_div = c1 / c2

# print(f"Addition: {result_add}")
# print(f"Subtraction: {result_sub}")
# print(f"Multiplication: {result_mul}")
# print(f"Division: {result_div}")

# # 3. Вам необходимо создать класс Airplane (самолет). 
# # С помощью перегрузки операторов реализовать: 
# # - Проверка на равенство типов самолетов (операция = =); 
# # - Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# # - Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > 
# # < <= >=).
# class Airplane:
#     def __init__(self, name, max_passengers, current_passengers):
#         self.name = name
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers

#     def __eq__(self, other):
#         return self.max_passengers == other.max_passengers

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers

#     def __add__(self, passengers):
#         new_passengers = self.current_passengers + passengers
#         if new_passengers <= self.max_passengers:
#             self.current_passengers = new_passengers
#         else:
#             print("Not enough capacity to add passengers.")

#     def __sub__(self, passengers):
#         new_passengers = self.current_passengers - passengers
#         if new_passengers >= 0:
#             self.current_passengers = new_passengers
#         else:
#             print("Passenger count cannot be negative.")

#     def __iadd__(self, passengers):
#         self.__add__(passengers)
#         return self

#     def __isub__(self, passengers):
#         self.__sub__(passengers)
#         return self

#     def __str__(self):
#         return f"{self.name} - Max Passengers: {self.max_passengers}, Current Passengers: {self.current_passengers}"
# plane1 = Airplane("Boeing 747", 416, 250)
# plane2 = Airplane("Airbus A380", 853, 500)
# print(plane1 == plane2)
# print(plane1 < plane2)
# print(plane1 <= plane2)
# print(plane1 > plane2)
# print(plane1 >= plane2)

# plane1 += 100
# print(plane1)

# plane2 -= 200
# print(plane2)

# 4. Создать класс Flat (квартира). Реализовать перегруженные операторы:
# - Проверка на равенство площадей квартир (операция ==);
# - Проверка на неравенство площадей квартир (операция !=);
# - Сравнение двух квартир по цене (операции > < <= >=).
class Flat:
    def __init__(self, name, area, price):
        self.name = name
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"{self.name} - Area: {self.area} sq. m, Price: ${self.price}"
flat1 = Flat("2-bedroom", 100, 150000)
flat2 = Flat("1-bedroom", 80, 120000)

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 > flat2)
print(flat1 >= flat2)
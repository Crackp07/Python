# # 1. К уже реализованному классу «Дробь» добавьте статический метод,
# # который при вызове возвращает количество созданных объектов класса «Дробь».
# class Fraction:
#     count = 0
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.count += 1
#     def display(self):
#         print(f"{self.numerator}/{self.denominator}")
#     @staticmethod
#     def count_objects():
#         return Fraction.count
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
# print("Fraction 1:")
# fraction1.display()
# print("Fraction 2:")
# fraction2.display()
# print(f"Total Fraction objects created: {Fraction.count_objects()}")

# # 2.Создайте класс для конвертирования температуры из
# # Цельсия в Фаренгейт и наоборот. У класса должно быть
# # два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.
# # Также класс должен считать количество подсчетов температуры и
# # возвращать это значение с помощью статического метода.
# class TempConverter:
#     count = 0 
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         TempConverter.count += 1
#         return (celsius * 9/5) + 35
#     @staticmethod
#     def  fahrenheit_to_celsius(fahrenheit):
#         TempConverter.count += 1
#         return (fahrenheit - 32) * 5/9
#     @staticmethod
#     def get_conversion_count():
#         return TempConverter.count
# celsius_temperature = 25
# fahrenheit_temperature = TempConverter.celsius_to_fahrenheit(celsius_temperature)
# print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")
# new_celsius_temperature = TempConverter.fahrenheit_to_celsius(fahrenheit_temperature)
# print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {new_celsius_temperature} degrees Celsius")
# print(f"Number of conversions: {TempConverter.get_conversion_count()}")

# # 3. Создайте класс для перевода из метрической системы
# # в английскую и наоборот. Функциональность необходимо
# # реализовать в виде статических методов. Обязательно
# # реализуйте перевод мер длины.
# class LengthConverter:
#     @staticmethod
#     def meters_to_feet(meters):
#         return meters * 3.28084 
#     @staticmethod
#     def feet_to_meters(feet):
#         return feet / 3.28084 
# meters_length = 10
# feet_length = LengthConverter.meters_to_feet(meters_length)
# print(f"{meters_length} meters equals {feet_length} feet")
# new_meters_length = LengthConverter.feet_to_meters(feet_length)
# print(f"{feet_length} feet equals {new_meters_length} meters")
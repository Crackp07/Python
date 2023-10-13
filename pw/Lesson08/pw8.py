# 1
# class Number:
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other):
#         return Number(self.value + other.value)
#     def __sub__(self,other):
#         return Number(self.value - other.value)
#     def __mul__(self,other):
#         return Number(self.value * other.value)
#     def __truediv__(self,other):
#         if other.value == 0:
#             print("Ділення на нуль не можливе.;)")
#         else:
#             return Number(self.value / other.value)
#     def __str__(self):
#         return str(self.value)
# a = Number(30)
# b = Number(0)

# result1 = a + b 
# print("Додавання:", result1)
# result2 = a - b
# print("Віднімання:", result2)
# result3 = a * b
# print("Множення:", result3)
# result4 = a / b
# print("Ділення:", result4)
# 2
class Fraction:
    def __init__(self, number1, number2):
        if number2 == 0:
            print("Знаменник не може бути рівним нулю.")
        self.number1 = number1
        self.number2 = number2
    def __add__(self, other):
        result_number1 = self.number1 * other.number2 + other.number1 * self.number2
        result_number2 = self.number2 * self.number2
        return Fraction(result_number1, result_number2)
    def __sub__(self, other):
        result_number1 = self.number1 * other.number2 - other.number1 * self.number2
        result_number2 = self.number2 * other.number2
        return Fraction(result_number1, result_number2)
    def __mul__(self,other):
        result_number1 = self.number1 * other.number1
        result_number2 = self.number2 * other.number2
        return Fraction(result_number1, result_number2)
    def __truediv__(self,other):
        if other.number1 == 0:
            print("Ділення на нуль не можливе.;)")
        result_number1 = self.number1 * other.number2
        result_number2 = self.number2 * other.number1
        return Fraction(result_number1, result_number2)
    def __str__(self):
        return f"{self.number1}/{self.number2}"
    
fraction1 = Fraction(10, 4)
fraction2 = Fraction(1, 4)

result1 = fraction1 + fraction2
print("Додавання:",result1)
result2 = fraction1 - fraction2
print("Віднімання:",result2)
result3 = fraction1 * fraction2
print("Множення:",result3)
result4 = fraction1 / fraction2
print("Ділення:",result4)
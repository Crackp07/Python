class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return Number(self.value + other.value)
    def __sub__(self,other):
        return Number(self.value - other.value)
    def __mul__(self,other):
        return Number(self.value * other.value)
    def __truediv__(self,other):
        if other.value == 0:
            print("Ділення на нуль не можливе.")
        else:
            return Number(self.value / other.value)
    def __str__(self):
        return str(self.value)
a = Number(30)
b = Number(0)

result1 = a + b 
print("Додавання:", result1)
result2 = a - b
print("Віднімання:", result2)
result3 = a * b
print("Множення:", result3)
result4 = a / b
print("Ділення", result4)
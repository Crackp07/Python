# 1
# # number = int(input("Введіть число: "))
# # if number % 2 == 0:
# #     print(number, "Even number")
# # else:
# #     print(number, "Odd number")
# 2
# number = int(input("Введіть число: "))
# if number % 7 == 0:
#     print(number, "Number is multiple 7")
# else:
#     print(number, "Number is not multiple 7")
# 3
# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
# if  number1 > number2:
#     maximum = number1
# else :
#     maximum = number2
# print("Максимум з чисел:", maximum)
# 4
# number1 = int(input("Введіть перше число: "))
# number2 = int(input("Введіть друге число: "))
# if number1 < number2:
#     minimum = number1
# else : minimum = number2
# print("Мінімум з чисел: ",minimum)
# 5
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
print("Виберіть операцію: ")
print("1. Сума: ")
print("2. Різниця: ")
print("3. Середнє арифметичне: ")
print("4. Добуток: ")
choice = int(input("Виберіть номер операції (1/2/3/4): "))
if choice == '1':
    result = number1 + number2
    operation = "Сума"
elif choice == '2':
    result = number1 - number2
    operation = "Різниця"
elif choice == '3':
    result = (number1 + number2) / 2
    operation = "Середнє арифметичне"
elif choice == '4':
    result = number1 * number2
    operation = "Добуток"
else : 
    print("Некоректний вибір операції")
    result = None
if result is not None:
    print(f"Результат {operation} чисел {number1} і {number2} дорівнює {result}")
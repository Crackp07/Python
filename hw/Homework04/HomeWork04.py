# # 1.Пользователь вводит с клавиатуры два числа (начало и конец диапазона). 
# # Требуется проанализировать все числа в этом диапазоне по следующему правилу: если 
# # число кратно 7, его надо выводить на экран.
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))
# for number in range(start, end + 1):
#     if number % 7 == 0:
#         print(number)
# # 2. Пользователь вводит с клавиатуры два числа (начало и конец диапазона). 
# # Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# # 1. Все числа диапазона;
# # 2. Все числа диапазона в убывающем порядке;
# # 3. Все числа, кратные 7;
# # 4. Количество чисел, кратных 5.
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))
# count_multiple_of_7 = 0
# count_multiple_of_5 = 0
# print("Всі числа діапазону:")
# for number in range(start, end + 1):
#     print(number)
# print("\nВсі числа діапазону в убывающем порядке:")
# for number in range(end, start - 1, -1):
#     print(number)
# print("\nВсі числа, кратні 7:")
# for number in range(start, end + 1):
#     if number % 7 == 0:
#         print(number)
#         count_multiple_of_7 += 1
# for number in range(start, end + 1):
#     if number % 5 == 0:
#         count_multiple_of_5 += 1
# print(f"\nКількість чисел, кратних 5: {count_multiple_of_5}")
# # 3. Пользователь вводит с клавиатуры два числа (начало 
# # и конец диапазона). Требуется проанализировать все числа 
# # в этом диапазоне. Вывод на экран должен проходить по 
# # правилам, указанным ниже.
# # Если число кратно 3 (делится на 3 без остатка) нужно 
# # вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. 
# # Если число кратно 3 и 5 нужно вывести 
# # Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести 
# # само число.
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))
# for number in range(start, end + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# # 4.Пользователь вводит с клавиатуры два числа. Нужно 
# # посчитать отдельно сумму четных, нечетных и чисел, 
# # кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))
# sum_even = 0
# sum_odd = 0
# sum_multiple_of_9 = 0
# count_even = 0
# count_odd = 0
# count_multiple_of_9 = 0
# for number in range(start, end + 1):
#     if number % 9 == 0:
#         sum_multiple_of_9 += number
#         count_multiple_of_9 += 1
#     elif number % 2 == 0:
#         sum_even += number
#         count_even += 1
#     else:
#         sum_odd += number
#         count_odd += 1
# average_even = sum_even / count_even if count_even > 0 else 0
# average_odd = sum_odd / count_odd if count_odd > 0 else 0
# average_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9 if count_multiple_of_9 > 0 else 0
# print(f"Сума парних чисел: {sum_even}")
# print(f"Сума непарних чисел: {sum_odd}")
# print(f"Сума чисел, кратних 9: {sum_multiple_of_9}")

# print(f"Середнє арифметичне парних чисел: {average_even}")
# print(f"Середнє арифметичне непарних чисел: {average_odd}")
# print(f"Середнє арифметичне чисел, кратних 9: {average_multiple_of_9}")
# # 5. Пользователь вводит с клавиатуры длину линии и 
# # символ для заполнения линии. Нужно отобразить на 
# # экране вертикальную линию из введенного символа, 
# # указанной длины. 
# # Например, если было введено 5 и символ %, тогда 
# # вывод на экран будет такой:
# #                            %
# #                            %
# #                            %
# #                            %
# #                            %
# length = int(input("Введіть довжину лінії: "))
# symbol = input("Введіть символ для заповнення лінії: ")
# for _ in range(length):
#     print(symbol)
# # 6. Пользователь вводит с клавиатуры числа. Если число 
# # больше нуля нужно вывести надпись «Number is positive», если меньше нуля «Number is negative», если равно нулю 
# # «Number is equal to zero». Когда пользователь вводит 
# # число 7 программа прекращает свою работу и выводит 
# # на экран надпись «Good bye!»
# while True:
#     number = int(input("Введіть число: "))
    
#     if number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")

#     if number == 7:
#         print("Good bye!")
#         break
# # 7. Пользователь вводит с клавиатуры числа. 
# # Программа должна подсчитывать сумму, максимум и минимум, 
# # введенных чисел. Когда пользователь вводит число 7 
# # программа прекращает свою работу и выводит на экран 
# # надпись «Good bye!»
# numbers = []
# while True:
#     number = input("Введіть число (або '7' для завершення): ")
#     if number == '7':
#         print("Good bye!")
#         break
#     else:
#         number = int(number)
#         numbers.append(number)
#     if len(numbers) > 0:
#         print(f"Сума введених чисел: {sum(numbers)}")
#         print(f"Максимум: {max(numbers)}")
#         print(f"Мінімум: {min(numbers)}")
# # 8. Напишите программу, которая запрашивает два 
# # целых числа x и y, после чего вычисляет и выводит 
# # значение x в степени y
# x = int(input("Введіть число x: "))
# y = int(input("Введіть ступінь y: "))
# result = x ** y
# print(f"{x} у степені {y} дорівнює {result}")
# # 9. Подсчитать количество целых чисел в диапазоне от 
# # 100 до 999 у которых есть две одинаковые цифры.
# count = 0
# for number in range(100, 1000):
#     digits = [int(digit) for digit in str(number)]  
#     if len(set(digits)) < 3:
#         count += 1
# print(f"Кількість чисел з двома однаковими цифрами в діапазоні від 100 до 999: {count}")
# # 10. Подсчитать количество целых чисел в диапазоне от 
# # 100 до 9999 у которых все цифры разные.
# count = 0
# for number in range(100, 10000):
#     digits = [int(digit) for digit in str(number)]
# if len(set(digits)) == len(digits):
#     count += 1
# print(f"Кількість чисел з різними цифрами в діапазоні від 100 до 9999: {count}")
# # 11. Пользователь вводит любое целое число. 
# # Необходимо из этого целого числа удалить все цифры 3 и 6 и 
# # вывести обратно на экран. 
# number = int(input("Введите целое число: "))
# number_str = str(number)
# result_str = ''.join(char for char in number_str if char not in ['3', '6'])
# result = int(result_str)
# print(f"Результат без цифр 3 и 6: {result}")

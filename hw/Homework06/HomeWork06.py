# # 1. Напишите функцию, которая отображает на экран 
# # форматированный текст, указанный ниже:
# # “Don't compare yourself with anyone in this world…
# # if you do so, you are insulting yourself.”
# # Bill Gates
# def display_quote():
#     quote = "Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself."
#     author = "Bill Gates"
#     print(quote)
#     print(author)
# display_quote()

# # 2. Напишите функцию, которая принимает два числа 
# # в качестве параметра и отображает все четные числа 
# # между ними.
# def display_even_numbers(start, end):
#     if start % 2 != 0:
#         start += 1
#     for number in range(start, end, 2):
#         print(number)
# start_num = int(input("Введіть початкове число: "))
# end_num = int(input("Введіть кінцеве число: "))
# print(f"Парні числа між {start_num} та {end_num}:")
# display_even_numbers(start_num, end_num)

# # 3. Напишите функцию, которая отображает пустой или 
# # заполненный квадрат из некоторого символа. Функция 
# # принимает в качестве параметров: длину стороны квадрата,
# # символ и переменную логического типа: 
# # - если она равна True, квадрат заполненный;
# # - если False, квадрат пустой.
# def draw_square(side_length, symbol, filled=True):
#     for i in range(side_length):
#         if filled:
#             print(symbol * side_length)
#         else:
#             if i == 0 or i == side_length - 1:
#                 print(symbol * side_length)
#             else:
#                 print(symbol + ' ' * (side_length - 2) + symbol)
# side = int(input("Введіть довжину сторони квадрата: "))
# character = input("Введіть символ для заповнення квадрата: ")
# fill_square = input("Заповненний квадрат (так/ні): ").lower() == "так"
# print("Ваш квадрат:")
# draw_square(side, character, fill_square)

# # 4. Напишите функцию, которая возвращает минимальное 
# # из пяти чисел. Числа передаются в качестве параметров.
# def find_min_of_five(a, b, c, d, e):
#     return min(a, b, c, d, e)
# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# num3 = int(input("Введіть третє число: "))
# num4 = int(input("Введіть четверте число: "))
# num5 = int(input("Введіть п'яте число: "))
# min_number = find_min_of_five(num1, num2, num3, num4, num5)
# print(f"Мінімальне число з введенних: {min_number}")

# # 5. Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. 
# # Границы диапазона передаются в качестве параметров. 
# # Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 — 
# # нижняя граница), их нужно поменять местами.
# def calculate_product_in_range(num1, num2):
#     if num1 > num2:
#         num1, num2 = num2, num1
#     product = 1
#     for num in range(num1, num2 + 1):
#         product *= num
#     return product
# lower_bound = int(input("Введіть нижню границю: "))
# upper_bound = int(input("Введіть верхню границю: "))
# result = calculate_product_in_range(lower_bound, upper_bound)
# print(f"Добуток чисел у заданому діапазоні: {result}")

# # 6. Напишите функцию, которая считает количество 
# # цифр в числе. Число передаётся в качестве параметра. Из 
# # функции нужно вернуть полученное количество цифр. 
# # Например, если передали 3456, количество цифр будет 4.
# def count_digits(number):
#     number_str = str(number)
#     digit_count = len(number_str)
#     return digit_count
# number = int(input("Введіть число: "))
# digit_count = count_digits(number)
# print(f"Кількість цифр у числі {number}: {digit_count}")

# # 7. Напишите функцию, которая проверяет является ли 
# # число палиндромом. Число передаётся в качестве параметра. 
# # Если число палиндром нужно вернуть из функции true, иначе false.
# # «Палиндром» — это число, у которого первая часть 
# # цифр равна второй перевернутой части цифр. Например, 
# # 123321 — палиндром (первая часть 123, вторая 321, которая 
# # после переворота становится 123), 546645 — палиндром, 
# # а 421987 — не палиндром. 
# def is_palindrome(number):
#     number_str = str(number)
#     reversed_str = number_str[::-1]
#     return number_str == reversed_str
# number = int(input("Введіть число: "))
# result = is_palindrome(number)
# if result:
#     print(f"{number} - це паліндром")
# else:
#     print(f"{number} - не паліндром")

# # 8. Напишите функцию, вычисляющую произведение 
# # элементов списка целых. Список передаётся в качестве параметра. 
# # Полученный результат возвращается из функции
# def product_of_elements(numbers):
#     result = 1
#     for number in numbers:
#         result *= number
#     return result
# my_list = [2, 3, 4, 5]
# result = product_of_elements(my_list)
# print(f"Добуток елементів списку: {result}")

# # 9. Напишите функцию для нахождения минимума в 
# # списке целых. Список передаётся в качестве параметра. 
# # Полученный результат возвращается из функции.
# def find_minimum(numbers):
#     if len(numbers) == 0:
#         return None
#     minimum = numbers[0]
#     for number in numbers:
#         if number < minimum:
#             minimum = number
#     return minimum
# my_list = [5, 2, 9, 1, 7]
# min_value = find_minimum(my_list)
# if min_value is not None:
#     print(f"Мінімум у списку: {min_value}")
# else:
#     print("Список порожній.")

# # 10. Напишите функцию, определяющую количество простых чисел в списке целых. 
# # Список передаётся в качестве параметра.
# # Полученный результат возвращается из функции
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def count_primes(numbers):
#     count = 0
#     for number in numbers:
#         if is_prime(number):
#             count += 1
#     return count
# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_count = count_primes(my_list)
# print(f"Кількість простих чисел у списку: {prime_count}")

# # 11. Напишите функцию, удаляющую из списка целых 
# # некоторое заданное число. Из функции нужно вернуть 
# # количество удаленных элементов.
# def remove_and_count(lst, number_to_remove):
#     count = 0
#     while number_to_remove in lst:
#         lst.remove(number_to_remove)
#         count += 1
#     return count
# my_list = [1, 2, 3, 4, 2, 5, 2, 6]
# number_to_remove = 2
# removed_count = remove_and_count(my_list, number_to_remove)
# print(f"Видалено {removed_count} елементів зі значенням {number_to_remove}")
# print("Список після видалення:", my_list)

# # 12. Напишите функцию, которая получает два списка в 
# # качестве параметра и возвращает список, содержащий 
# # элементы обоих списков.
# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = merge_lists(list1, list2)
# print(result)

# # 13. Напишите функцию, высчитывающую степень каждого 
# # элемента списка целых. Значение для степени передаётся 
# # в качестве параметра, список тоже передаётся в качестве 
# # параметра. Функция возвращает новый список, содержащий полученные результаты.
# def calculate_powers(numbers, exponent):
#     powered_list = [number ** exponent for number in numbers]
#     return powered_list
# numbers = [1, 2, 3, 4]
# exponent = 2
# result = calculate_powers(numbers, exponent)
# print(result)

# # 14. Написать рекурсивную функцию нахождения 
# # наибольшего общего делителя двух целых чисел
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# num1 = 48
# num2 = 18
# result = gcd(num1, num2)
# print(f"НСД чисел {num1} і {num2} дорівнює {result}")

# # 15. Написать игру «Быки и коровы». 
# # Программа «загадывает» четырёхзначное число и играющий должен угадать его. 
# # После ввода пользователем числа программа 
# # сообщает, сколько цифр числа угадано (быки) и сколько 
# # цифр угадано и стоит на нужном месте (коровы).
# # После отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. 
# # В программе необходимо использовать рекурсию.
# import random
# def generate_secret_number():
#     return str(random.randint(1000, 9999))
# def count_bulls_and_cows(secret, guess):
#     bulls, cows = 0, 0
#     for i in range(4):
#         if guess[i] == secret[i]:
#             bulls += 1
#         elif guess[i] in secret:
#             cows += 1
#     return bulls, cows

# def play_game(secret, attempts=1):
#     print(f"Спроба {attempts}")
#     guess = input("Введіть своє припущення (4-значне число): ")
#     if guess == secret:
#         print(f"Щиро вітаю! Ви вгадали число {secret} в {attempts} спроби.")
#     else:
#         bulls, cows = count_bulls_and_cows(secret, guess)
#         print(f"Бики: {bulls}, Корови: {cows}\n")
#         play_game(secret, attempts + 1)
# if __name__ == "__main__":
#     secret_number = generate_secret_number()
#     print("Ласкаво просимо в гру Бики та Корови! Спробуйте вгадати 4-значне число.")
#     play_game(secret_number)

# # 16. Дана шахматная доска размером 8×8 и шахматный конь. 
# # Программа должна запросить у пользователя координаты 
# # клетки поля и поставить туда коня. Задача программы 
# # найти и вывести путь коня, при котором он обойдет все 
# # клетки доски, становясь в каждую клетку только один 
# # раз. (Так как процесс отыскания пути для разных начальных клеток может затянуться,
# # то рекомендуется сначала опробовать задачу на поле размером 6×6). В программе 
# # необходимо использовать рекурсию.
import numpy as np

def is_valid_move(x, y, board):
    if x >= 0 and x < board.shape[0] and y >= 0 and y < board.shape[1] and board[x, y] == -1:
        return True
    return False
def print_board(board):
    for row in board:
        print(' '.join([f'{cell:2}' for cell in row]))
def knight_tour(board, x, y, move_count):
    if move_count == board.size:
        print_board(board)
        return True
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if is_valid_move(new_x, new_y, board):
            board[new_x, new_y] = move_count
            if knight_tour(board, new_x, new_y, move_count + 1):
                return True
            board[new_x, new_y] = -1
    return False
def main():
    n = 6 #при 8 дуже довго думає, тому поставив 6
    start_x = int(input("Введіть початкову координату X: "))
    start_y = int(input("Введіть початкову координату Y: "))
    if start_x < 0 or start_x >= n or start_y < 0 or start_y >= n:
        print("Введені координати поза діапазоном доски.")
        return
    board = np.full((n, n), -1)
    board[start_x, start_y] = 0
    if knight_tour(board, start_x, start_y, 1):
        print("Шлях знайдено!")
    else:
        print("шлях не знайдено.")
if __name__ == "__main__":
    main()


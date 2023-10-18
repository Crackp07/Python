# # 1. Пользователь вводит с клавиатуры строку. Проверьте 
# # является ли введенная строка палиндромом. 
# # Палиндром — слово или текст, которое читается одинаково 
# # слева направо и справа налево. Например, кок; А роза 
# # упала на лапу Азора; доход; А буду я у дуба.
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s [::-1]
# user_input = input("Введіть рядок: ")
# if is_palindrome(user_input):
#     print("Цей рядок є паліндромом.")
# else:
#     print("Цей рядок не є паліндромом.")

# # 2. Пользователь вводит с клавиатуры некоторый текст, 
# # после чего пользователь вводит список зарезервированных 
# # слов. Необходимо найти в тексте все зарезервированные 
# # слова и изменить их регистр на верхний. Вывести на 
# # экран измененный текст.
# text = input("Введіть текст: ")
# reserved_words = input("Введіть список зарезервованих слів, розділених пробілами: ").split()
# words = text.split()
# for i in range(len(words)):
#     if words[i].lower() in [word.lower() for word in reserved_words]:
#         words[i] = words[i].upper()
# modified_text = " ".join(words)
# print("Змінений текст:")
# print(modified_text)

# # 3. Есть некоторый текст. 
# # Посчитайте в этом тексте 
# # количество предложений и 
# # выведите на экран полученный результат.
# import nltk
# nltk.download('punkt')
# text = input("Введіть текст: ")
# sentences = nltk.sent_tokenize(text)
# num_sentences = len(sentences)
# print(f"Кількість речень в тексті: {num_sentences}")

# # 4. Пользователь вводит с клавиатуры арифметическое 
# # выражение. Например, 23+12.
# # Необходимо вывести на экран результат выражения. 
# # В нашем примере это 35. Арифметическое выражение 
# # может состоять только из трёх частей: число, операция, 
# # число. Возможные операции: +, -,*,/
# expression = input("Введіть арифметичний вираз: ")
# try:
#     result = eval(expression)
#     print(f"Результат: {result}")
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль.")
# except SyntaxError:
#     print("Помилка в арифметичному виразі.")

# # 5. В списке целых, заполненном случайными числами, 
# # определить минимальный и максимальный элементы, 
# # посчитать количество отрицательных элементов, 
# # посчитать количество положительных элементов, посчитать 
# # количество нулей. Результаты вывести на экран.
# import random
# random_list = [random.randint(-10, 10) for _ in range(20)]
# min_value = float('inf')
# max_value = float('-inf')
# negative_count = 0
# positive_count = 0
# zero_count = 0
# for num in random_list:
#     if num < min_value:
#         min_value = num
#     if num > max_value:
#         max_value = num
#     if num < 0:
#         negative_count += 1
#     elif num > 0:
#         positive_count += 1
#     else:
#         zero_count += 1
# print(f"Мінімум: {min_value}")
# print(f"Максимум: {max_value}")
# print(f"Кількість від'ємних чисел: {negative_count}")
# print(f"Кількість позитивних чисел: {positive_count}")
# print(f"Кількість нулів: {zero_count}")

# # 6. Два списка целых заполняются случайными числами.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# # Необходимо:
# # Сформировать третий список, содержащий элементы 
# # обоих списков;
# list3 = list1 + list2
# print(list3)
# # Сформировать третий список, содержащий элементы 
# # обоих списков без повторений;
# list3 = list(set(list1 + list2))
# print(list3)
# # Сформировать третий список, содержащий элементы 
# # общие для двух списков;
# list3 = list(set(list1) & set(list2))
# print(list3)
# # Сформировать третий список, содержащий только 
# # уникальные элементы каждого из списков;
# unique_list1 = list(set(list1))
# unique_list2 = list(set(list2))
# list3 = unique_list1 + unique_list2
# print(list3)
# # Сформировать третий список, содержащий только 
# # минимальное и максимальное значение каждого из 
# # списков.
# min_max_list1 = [min(list1), max(list1)]
# min_max_list2 = [min(list2), max(list2)]
# list3 = min_max_list1 + min_max_list2
# print(list3)
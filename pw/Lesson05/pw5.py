# 1
# input_string = input("Введіть рядок: ")
# reversed_string = input_string[::-1]
# print("Обернутий рядок:", reversed_string)
# 2
input_string = input("Введіть рядок: ")
letter_count = 0
digit_count = 0
for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print("Кількість букв у рядку:", letter_count)
print("Кількість чисел у рядку:", digit_count) 
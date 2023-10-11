# 1
# num1 = int(input('Введіть перше чисто: '))
# num2 = int(input('Введіть друге число: '))
# num3 = int(input('Введіть трете число: '))
# sum_result = num1 + num2 + num3
# product_result = num1 * num2 * num3
# print('Сумма чисел: ', sum_result)
# print('Произведение чисел: ', product_result)
# 2
# zarplata = int(input("Зарплата за місяць: "))
# kredit = int(input("Сума місячного платежу по кредиту: "))
# komunalni_poslugi = int(input("Задолженісь за комунальні послуги: "))
# zalishok = zarplata - kredit - komunalni_poslugi
# print("Залишок після виплат: ", zalishok)
# 3
# D1 = int(input("Введіть довжину першої діагоналі ромба: "))
# D2 = int(input("Введіть довжину другої діагоналі ромба: "))
# area = (D1 * D2)/2
# print(f"Площа ромба з діагоналями {D1} і {D2} дорівню {area}")
# 4
# print("To be\nor not\nto be")
# 5
# quote = "Life is what happens\nwhen\nyou're busy making other plans\nJohn Lennon."
# print(quote)
# 6
# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# c = int(input("Введіть третє число: "))
# result = a * 100 + b * 10 + c 
# print("Створене чило: ", result)
# 7
# number = int(input("Введіть число з чотирьох цифр: "))
# a = number // 1000
# b = (number % 1000) // 100
# c = (number % 100) // 10
# d = number % 10
# product = a * b * c * d
# print(f"Результат добутку цифр: {a}*{b}*{c}*{d}={product}")
# 8
# met = int(input("Введіть кількість метрі: "))
# centimet = met * 100
# decimet = met * 10
# millimet = met * 1000
# miles = met * 0.000621371
# print(f"{met} метрів дорівнює {centimet} сантиметрів")
# print(f"{met} метрів дорівнює {decimet} дециметрів")
# print(f"{met} метрів дорівнює {millimet} міліметрів")
# print(f"{met} метрів дорівнює {miles} миль")
# 9
# l = int(input("Введіть довжину основи трикутника: "))
# h = int(input("Введіть довжину висоти трикутника: "))
# s = (l*h)/2
# print(f"Площа трикутнака дорівнює", s) 
# 10
n = int(input("Введіть чотирьохзначне число: "))
a = n % 10
b = (n // 10) % 10
c = (n // 100) % 10
d = (n // 1000) % 10
reversed_number = a * 1000 + b * 100 + c * 10 + d
print(f"Результат перевертання числа: ", reversed_number)
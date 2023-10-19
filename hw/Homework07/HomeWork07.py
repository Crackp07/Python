# # 1. Реализуйте класс «Автомобиль». Необходимо хранить 
# # в полях класса: название модели, год выпуска,
# # производителя, объем двигателя, цвет машины, цену. 
# # Реализуйте методы класса для ввода данных, вывода данных, 
# # реализуйте доступ к отдельным полям через методы клаccа
# class Car: 
#     def __init__(self, model, year, manufacturer, engine_size, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_size = engine_size
#         self.color = color
#         self.price = price
#     def set_model(self, model):
#         self.model = model
#     def set_year(self, year):
#         self.year = year
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#     def set_engine_size(self, engine_size):
#         self.engine_size = engine_size
#     def set_color(self, color):
#         self.color = color
#     def set_price(self, price):
#         self.price = price
#     def get_model(self):
#         return self.model
#     def get_year(self):
#         return self.year
#     def get_manufacturer(self):
#         return self.manufacturer
#     def get_engine_size(self):
#         return self.engine_size
#     def get_color(self):
#         return self.color
#     def get_price(self):
#         return self.price
#     def display_info(self):
#         print(f"Модель: {self.model}")
#         print(f"Рік випуску: {self.year}")
#         print(f"Виробник: {self.manufacturer}")
#         print(f"Об'єм двигуна: {self.engine_size}")
#         print(f"Колір: {self.color}")
#         print(f"Ціна: {self.price}")
# my_car = Car("Toyota Camry", 2022, "Toyota", 2.5, "Срібний", 25000)
# my_car.display_info()

# my_car.set_model("Honda Accord")
# my_car.set_price(22000)
# my_car.display_info()

# # 2. Реализуйте класс «Книга». Необходимо хранить в 
# # полях класса: название книги, год выпуска, издателя, 
# # жанр, автора, цену. Реализуйте методы класса для ввода 
# # данных, вывода данных, реализуйте доступ к отдельным 
# # полям через методы класса
# class Book:
#     def __init__(self, title, year, publisher, genre, author, price):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price

#     def set_title(self, title):
#         self.title = title

#     def set_year(self, year):
#         self.year = year

#     def set_publisher(self, publisher):
#         self.publisher = publisher

#     def set_genre(self, genre):
#         self.genre = genre

#     def set_author(self, author):
#         self.author = author

#     def set_price(self, price):
#         self.price = price

#     def get_title(self):
#         return self.title

#     def get_year(self):
#         return self.year

#     def get_publisher(self):
#         return self.publisher

#     def get_genre(self):
#         return self.genre

#     def get_author(self):
#         return self.author

#     def get_price(self):
#         return self.price

#     def display_info(self):
#         print(f"Назва книги: {self.title}")
#         print(f"Рік видання: {self.year}")
#         print(f"Видавець: {self.publisher}")
#         print(f"Жанр: {self.genre}")
#         print(f"Автор: {self.author}")
#         print(f"Ціна: {self.price}")
# my_book = Book("Тіні забуихих предків", 2013, "Український мессенджер", "Проза", "Михайло Коцюбинський", 40)
# my_book.display_info()
# my_book.set_title("Тигролови")
# my_book.set_author("Іван Багряний")
# my_book.display_info()

# # 3. Реализуйте класс «Стадион». Необходимо хранить в 
# # полях класса: название стадиона, дату открытия, страну, 
# # город, вместимость. Реализуйте методы класса для ввода 
# # данных, вывода данных, реализуйте доступ к отдельным 
# # полям через методы класса.
# class Stadium:
#     def __init__(self, name, opening_date, country, city, capacity):
#         self.name = name
#         self.opening_date = opening_date
#         self.country = country
#         self.city = city
#         self.capacity = capacity

#     def set_name(self, name):
#         self.name = name

#     def set_opening_date(self, opening_date):
#         self.opening_date = opening_date

#     def set_country(self, country):
#         self.country = country

#     def set_city(self, city):
#         self.city = city

#     def set_capacity(self, capacity):
#         self.capacity = capacity

#     def get_name(self):
#         return self.name

#     def get_opening_date(self):
#         return self.opening_date

#     def get_country(self):
#         return self.country

#     def get_city(self):
#         return self.city

#     def get_capacity(self):
#         return self.capacity

#     def display_info(self):
#         print(f"Назва стадіону: {self.name}")
#         print(f"Дата відкриття: {self.opening_date}")
#         print(f"Країна: {self.country}")
#         print(f"Місто: {self.city}")
#         print(f"Вмістимість: {self.capacity} осіб")
# stadium = Stadium("Олімпійський", "1972-08-20", "Україна", "Київ", 70050)
# stadium.display_info()

# stadium.set_name("НСК Олімпійський")
# stadium.set_city("Львів")
# stadium.display_info()

# # 4. К уже реализованному классу «Автомобиль» добавьте 
# # конструктор, а также необходимые перегруженные методы.
# class Car:
#     def __init__(self, model, year, manufacturer, engine_size, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_size = engine_size
#         self.color = color
#         self.price = price

#     def __str__(self):
#         return f"Модель: {self.model}, Рік випуску: {self.year}, Виробник: {self.manufacturer}, Об'єм двигуна: {self.engine_size}, Колір: {self.color}, Ціна: {self.price}"

#     def __eq__(self, other):
#         return self.price == other.price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __le__(self, other):
#         return self.price <= other.price

#     def __gt__(self, other):
#         return self.price > other.price

#     def __ge__(self, other):
#         return self.price >= other.price

#     def __ne__(self, other):
#         return self.price != other.price

# my_car = Car("Toyota Camry", 2022, "Toyota", 2.5, "Срібний", 25000)
# my_car2 = Car("Honda Accord", 2022, "Honda", 2.0, "Чорний", 27000)
# print(my_car)
# print(my_car2)
# print(my_car == my_car2)
# print(my_car < my_car2)

# # 5. К уже реализованному классу «Книга» добавьте конструктор,
# # а также необходимые перегруженные методы.
# class Book:
#     def __init__(self, title, year, publisher, genre, author, price):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"Назва книги: {self.title}, Рік видання: {self.year}, Видавець: {self.publisher}, Жанр: {self.genre}, Автор: {self.author}, Ціна: {self.price}"

#     def __eq__(self, other):
#         return self.price == other.price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __le__(self, other):
#         return self.price <= other.price

#     def __gt__(self, other):
#         return self.price > other.price

#     def __ge__(self, other):
#         return self.price >= other.price

#     def __ne__(self, other):
#         return self.price != other.price

# my_book = Book("Тіні забутих предків", 2013, "Український мессенджер", "Проза", "Михайло Коцюбинський", 40)
# my_book2 = Book("Тигролови", 1929, "Веселка", "Проза", "Іван Багряний", 60)
# print(my_book)
# print(my_book2)
# print(my_book == my_book2)
# print(my_book < my_book2)

# # 6. К уже реализованному классу «Стадион» добавьте 
# # конструктор, а также необходимые перегруженные методы.
# class Stadium:
#     def __init__(self, name, opening_date, country, city, capacity):
#         self.name = name
#         self.opening_date = opening_date
#         self.country = country
#         self.city = city
#         self.capacity = capacity

#     def __str__(self):
#         return f"Назва стадіону: {self.name}, Дата відкриття: {self.opening_date}, Країна: {self.country}, Місто: {self.city}, Вмістимість: {self.capacity} осіб"

#     def __eq__(self, other):
#         return self.capacity == other.capacity

#     def __lt__(self, other):
#         return self.capacity < other.capacity

#     def __le__(self, other):
#         return self.capacity <= other.capacity

#     def __gt__(self, other):
#         return self.capacity > other.capacity

#     def __ge__(self, other):
#         return self.capacity >= other.capacity

#     def __ne__(self, other):
#         return self.capacity != other.capacity

# stadium1 = Stadium("Олімпійський", "1972-08-20", "Україна", "Київ", 70050)
# stadium2 = Stadium("НСК Олімпійський", "2011-10-12", "Україна", "Львів", 34000)
# print(stadium1)
# print(stadium2)
# print(stadium1 == stadium2)
# print(stadium2 < stadium1)

# # 7. Реализуйте класс «Человек». Необходимо хранить в 
# # полях класса: ФИО, дату рождения, контактный телефон, 
# # город, страну, домашний адрес. Реализуйте методы класса 
# # для ввода данных, вывода данных, реализуйте доступ к 
# # отдельным полям через методы класса.
# class Person:
#     def __init__(self):
#         self.full_name = ""
#         self.birth_date = ""
#         self.phone = ""
#         self.city = ""
#         self.country = ""
#         self.address = ""

#     def input_data(self):
#         self.full_name = input("Введіть ім'я та прізвище: ")
#         self.birth_date = input("Введіть дату народження: ")
#         self.phone = input("Введіть контактний телефон: ")
#         self.city = input("Введіть місто: ")
#         self.country = input("Введіть країну: ")
#         self.address = input("Введіть домашню адресу: ")

#     def display_data(self):
#         print("Ім'я та прізвище:", self.full_name)
#         print("Дата народження:", self.birth_date)
#         print("Телефон:", self.phone)
#         print("Місто:", self.city)
#         print("Країна:", self.country)
#         print("Адреса:", self.address)

#     def get_full_name(self):
#         return self.full_name

#     def get_birth_date(self):
#         return self.birth_date

#     def get_phone(self):
#         return self.phone

#     def get_city(self):
#         return self.city

#     def get_country(self):
#         return self.country

#     def get_address(self):
#         return self.address
# person = Person()
# person.input_data()
# print("\nВведені дані:")
# person.display_data()

# # 8. Создайте класс «Город». Необходимо хранить в полях класса: название города, 
# # название региона, название страны, количество жителей в городе, 
# # почтовый индекс города, телефонный код города. 
# # Реализуйте методы класса для ввода данных,
# # вывода данных, реализуйте доступ к 
# # отдельным полям через методы класса.
# class City:
#     def __init__(self):
#         self.city_name = ""
#         self.region_name = ""
#         self.country_name = ""
#         self.population = 0
#         self.postal_code = ""
#         self.phone_code = ""

#     def input_data(self):
#         self.city_name = input("Введіть назву міста: ")
#         self.region_name = input("Введіть назву регіону: ")
#         self.country_name = input("Введіть назву країни: ")
#         self.population = int(input("Введіть кількість жителів в місті: "))
#         self.postal_code = input("Введіть поштовий індекс міста: ")
#         self.phone_code = input("Введіть телефонний код міста: ")

#     def display_data(self):
#         print("Назва міста:", self.city_name)
#         print("Назва регіону:", self.region_name)
#         print("Назва країни:", self.country_name)
#         print("Кількість жителів:", self.population)
#         print("Поштовий індекс:", self.postal_code)
#         print("Телефонний код:", self.phone_code)

#     def get_city_name(self):
#         return self.city_name

#     def get_region_name(self):
#         return self.region_name

#     def get_country_name(self):
#         return self.country_name

#     def get_population(self):
#         return self.population

#     def get_postal_code(self):
#         return self.postal_code

#     def get_phone_code(self):
#         return self.phone_code

# city = City()
# city.input_data()
# print("\nВведені дані про місто:")
# city.display_data()

# # 9. Создайте класс «Страна». Необходимо хранить в 
# # полях класса: название страны, название континента, 
# # количество жителей в стране, телефонный код страны, 
# # название столицы, название городов страны. Реализуйте 
# # методы класса для ввода данных, вывода данных, 
# # реализуйте доступ к отдельным полям через методы класса. 
# class Country:
#     def __init__(self):
#         self.country_name = ""
#         self.continent_name = ""
#         self.population = 0
#         self.phone_code = ""
#         self.capital_name = ""
#         self.cities = []

#     def input_data(self):
#         self.country_name = input("Введіть назву країни: ")
#         self.continent_name = input("Введіть назву континенту: ")
#         self.population = int(input("Введіть кількість жителів в країні: "))
#         self.phone_code = input("Введіть телефонний код країни: ")
#         self.capital_name = input("Введіть назву столиці: ")
        
#         num_of_cities = int(input("Введіть кількість міст в країні: "))
#         self.cities = [input(f"Назва міста {i + 1}: ") for i in range(num_of_cities)]

#     def display_data(self):
#         print("Назва країни:", self.country_name)
#         print("Назва континенту:", self.continent_name)
#         print("Кількість жителів:", self.population)
#         print("Телефонний код:", self.phone_code)
#         print("Назва столиці:", self.capital_name)
#         print("Назви міст в країні:")
#         for city in self.cities:
#             print(city)

#     def get_country_name(self):
#         return self.country_name

#     def get_continent_name(self):
#         return self.continent_name

#     def get_population(self):
#         return self.population

#     def get_phone_code(self):
#         return self.phone_code

#     def get_capital_name(self):
#         return self.capital_name

#     def get_cities(self):
#         return self.cities

# country = Country()
# country.input_data()
# print("\nВведені дані про країну:")
# country.display_data()

# # 10. Создайте класс «Дробь». Необходимо хранить в полях 
# # класса: числитель и знаменатель. Реализуйте методы класса 
# # для ввода данных, вывода данных, реализуйте доступ к 
# # отдельным полям через методы класса. Также создайте 
# # методы класса для выполнения арифметических операций 
# # (сложение, вычитание, умножение, деление, и т.д)
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator

#     def input_data(self):
#         self.numerator = int(input("Введіть чисельник: "))
#         self.denominator = int(input("Введіть знаменник: "))

#     def display_data(self):
#         print(f"{self.numerator}/{self.denominator}")

#     def get_numerator(self):
#         return self.numerator

#     def get_denominator(self):
#         return self.denominator

#     def add(self, other_fraction):
#         result_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
#         result_denominator = self.denominator * other_fraction.denominator
#         return Fraction(result_numerator, result_denominator)

#     def subtract(self, other_fraction):
#         result_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
#         result_denominator = self.denominator * other_fraction.denominator
#         return Fraction(result_numerator, result_denominator)

#     def multiply(self, other_fraction):
#         result_numerator = self.numerator * other_fraction.numerator
#         result_denominator = self.denominator * other_fraction.denominator
#         return Fraction(result_numerator, result_denominator)

#     def divide(self, other_fraction):
#         result_numerator = self.numerator * other_fraction.denominator
#         result_denominator = self.denominator * other_fraction.numerator
#         return Fraction(result_numerator, result_denominator)
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
# print("Дріб 1:")
# fraction1.display_data()
# print("Дріб 2:")
# fraction2.display_data()

# sum_fraction = fraction1.add(fraction2)
# print("Сума дробів:")
# sum_fraction.display_data()

# difference_fraction = fraction1.subtract(fraction2)
# print("Різниця дробів:")
# difference_fraction.display_data()

# product_fraction = fraction1.multiply(fraction2)
# print("Добуток дробів:")
# product_fraction.display_data()

# quotient_fraction = fraction1.divide(fraction2)
# print("Частка дробів:")
# quotient_fraction.display_data()

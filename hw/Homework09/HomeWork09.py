# # 1. Создайте класс Device, который содержит информацию об устройстве.
# # С помощью механизма наследования, реализуйте класс
# # CoffeeMachine (содержит информацию о кофемашине),
# # класс Blender (содержит информацию о блендере), класс
# # MeatGrinder (содержит информацию о мясорубке).
# # Каждый из классов должен содержать необходимые
# # для работы методы.
# class Device:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def turn_on(self):
#         print(f"{self.brand} {self.model} is turned on.")
#     def turn_off(self):
#         print(f"{self.brand} {self.model} is turned off.")
# class CoffeeMachine(Device):
#     def __init__(self, brand, model, coffee_type):
#         super().__init__(brand, model)
#         self.coffee_type = coffee_type
#     def make_coffee(self):
#         print(f"Making {self.coffee_type} coffee with {self.brand} {self.model}.")
# class Blender(Device):
#     def __init__(self, brand, model, speed):
#         super().__init__(brand, model)
#         self.speed = speed
#     def blend(self):
#         print(f"Blending at speed {self.speed} with {self.brand} {self.model}.")
# class MeatGrinder(Device):
#     def __init__(self, brand, model, grind_type):
#         super().__init__(brand, model)
#         self.grind_type = grind_type
#     def grind_meat(self):
#         print(f"Grinding {self.grind_type} with {self.brand} {self.model}.")
# coffee_machine = CoffeeMachine("Siemens", "TE653", "Americano")
# coffee_machine.turn_on()
# coffee_machine.make_coffee()
# coffee_machine.turn_off()
# blender = Blender("Tefal", "HB94L", "High")
# blender.turn_on()
# blender.blend()
# blender.turn_off()
# meat_grinder = MeatGrinder("Xiaomi", "MR9401", "Coarse")
# meat_grinder.turn_on()
# meat_grinder.grind_meat()
# meat_grinder.turn_off()

# # 2. Создайте класс Ship, который содержит информацию
# # о корабле.
# # С помощью механизма наследования, реализуйте
# # класс Frigate (содержит информацию о фрегате), класс
# # Destroyer (содержит информацию об эсминце), класс
# # Cruiser (содержит информацию о крейсере).
# # Каждый из классов должен содержать необходимые
# # для работы методы.
# class Ship:
#     def __init__(self, name, lenght, speed):
#         self.name = name
#         self.lenght = lenght
#         self.speed = speed
#     def start_engine(self):
#         print(f"{self.name} is starting engines.")
#     def stop_engine(self):
#         print(f"{self.name} is stopping engines.")
# class Frigate(Ship):
#         def __init__(self, name, lenght, speed, missile_count):
#             super().__init__(name, lenght, speed)
#             self.missile_count = missile_count
#         def fire_missiles(self):
#             print(f"{self.name} fires {self.missile_count} missiles.")
# class Destroyer(Ship):
#         def __init__(self, name, lenght, speed, gun_count):
#             super().__init__(name, lenght, speed)
#             self.gun_count = gun_count
#         def fire_guns(self):
#             print(f"{self.name} fires {self.gun_count} guns.")
# class Cruiser(Ship):
#         def __init__(self, name, lenght, speed, aircraft_count):
#             super().__init__(name, lenght, speed)
#             self.aircraft_count = aircraft_count
#         def launch_aircraft(self):
#             print(f"{self.name} launches {self.aircraft_count} aircraft.")
# frigate = Frigate("Knox", 134, 27, 12)
# frigate.start_engine()
# frigate.fire_missiles()
# frigate.stop_engine()

# destroyer = Destroyer("Zumwalt", 183, 30, 2)
# destroyer.start_engine()
# destroyer.fire_guns()
# destroyer.stop_engine()

# cruiser = Cruiser("Port Royal", 173, 32, 2)
# cruiser.start_engine()
# cruiser.launch_aircraft()
# cruiser.stop_engine()

# # 3.Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# # В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# # поле для хранения копеек (центы, евроценты, копейки
# # и т.д.).
# # Реализовать методы для вывода суммы на экран, задания значений для частей. 
# class Money:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#     def display(self):
#         print(f"${self.dollars}.{self.cents:02}")
#     def set_dollars(self, dollars):
#         self.dollars = dollars
#     def set_cents(self, cents):
#         if 0 <= cents <= 99:
#             self.cents = cents
#         else:
#             print("Invalid cents value. Cents should be in the range [0, 99].")
#     def add(self, other):
#         total_cents = self.dollars * 100 + self.cents + other.dollars * 100 + other.cents
#         self.dollars = total_cents // 100
#         self.cents = total_cents % 100
#     def subtract(self, other):
#         total_cents = self.dollars * 100 + self.cents - (other.dollars * 100 + other.cents)
#         if total_cents < 0:
#             print("Subtraction results in a negative value.")
#         else:
#             self.dollars = total_cents // 100
#             self.cents = total_cents % 100
# money1 = Money(10, 50)
# money2 = Money(5, 75)

# print("Money1:")
# money1.display()
# print("Money2:")
# money2.display()
# money1.add(money2)
# print("Money1 after adding Money2:")
# money1.display()
# money2.subtract(money1)
# print("Money2 after subtracting Money1:")
# money2.display()
# money1.set_cents(75)
# print("Money1 after changing cents:")
# money1.display()
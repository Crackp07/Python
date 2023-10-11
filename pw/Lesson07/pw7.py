# 1
# class Human:
#     def __init__(self):
#         self.fullname = ''
#         self.phone = ''
#         self.birthday = ''
#         self.city = ''
#         self.country = ''
#         self.homeadress = ''

#     def getFullname(self):
#         return self.fullname
#     def getPhone(self):
#         return self.phone
#     def getBirthday(self):
#         return self.birthday
#     def getCity(self):
#         return self.city
#     def getCountry(self):
#         return self.country
#     def getHomeadress(self):
#         return self.homeadress
    
#     def inputdata(self):
#         self.fullname = input("Введіть повне ім'я: ")
#         self.phone = input("Ведіть номер телефона: ")
#         self.birthday = input("Введіть дату народження: ")
#         self.city = input("Введіть місто: ")
#         self.country = input("Введіть країну: ")
#         self.homeadress = input("Введіть домашню адресу: ")

#     def showdata(self):
#         print("Повне ім'я: ", self.fullname)
#         print("Номер телефону: ", self.phone)
#         print("Дата народження: ", self.birthday)
#         print("Країна: ", self.country)
#         print("Місто: ", self.city)
#         print("Домашня адреса: ", self.homeadress)

# h1 = Human()
# h1.inputdata()
# print("\nВведені дані: ") 
# h1.showdata()
# # для отримання окремих полів
# print("\nПовне ім'я:",h1.getFullname())
# print("Дата народження:", h1.getBirthday())
# print("Номер телефону: ", h1.getPhone())
# print("Країна: ", h1.getCountry())
# print("Місто: ", h1.getCity())
# print("Домашня адреса: ", h1.getHomeadress())
# 2
# class City:
#     def __init__(self):
#         self.city = ''
#         self.region = ''
#         self.country = ''
#         self.population = 0
#         self.postcode = ''
#         self.phonecode = ''
#     def inputdata(self):

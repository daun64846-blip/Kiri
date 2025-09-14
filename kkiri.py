# class Dog:
#    def data(self, name):
#    print(name, "Gav", selg.age)
# self.age=7


# dog1.data("Bobik", sex "m")
# dog1 = Dog()
#
# dog2 = Dog()
# dog2.data("Tuzik", sex "w")


# def data(name):
#     print(name, "Gav")
# a = data("Tuzik")
# age =5


# class Dog:
#    def __init__(self, name, sex):
#    print(name, "Gav", selg.age)
# self.age=7
#
# dog1 = Dog (name"Tuzik", sex "m")
#
# dog2 = Dog(name "Bobita", sex "w"

# class Dog:
#    def __init__(self, name, age):
#    self.a = name
#    self.b = age
#
# dog1 = Dog("Tuzik", age = 6)
#
# print(self.a)
# print(self.b)

# class Price_fruit:
#
#     def __init__(self, fruit_name):
#         print("Фрукт", fruit_name )
#
#     def price(self, fruit_price):
#         print("Ціна", fruit_price)
#
#
# apple = Price_fruit("Яблуко")
# apple.price("12 грн")
#
# lemon = Price_fruit("Лимон")
# lemon.price("8 грн")

class Car:

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print("Car Information")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

car1 = Car("Toyota", "Camry", 2022, "Silver")
car2 = Car("Ford", "Mustang", 1969, "Red")
car3 = Car("Tesla", "Model 3", 2024, "Black")

car1.display_info()
car2.display_info()
car3.display_info()


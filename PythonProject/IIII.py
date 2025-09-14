# my_list = [1, 2, 8]
#
# print(my_list)
#
# my_list.append("СУХАРИКИИИИ")
#
# # print(my_list[1])
#
# for i in my_list:
#     print(i)
#
# a = "Hello"
#
# for i in a:
#     print(i)
#
# for i in  1, 2, 4, 10
#     print(i)

# def my_func(name, age)
#     print((f"{name} is {age} years old"))
#
#     my_func(name="John", age=25)
#
# def my_func(name, age):
#         return f"{name} is {age} years old"
#
# #     print(my_func(name="ann", age=26))
#
# def my_func(*args):
#     print(args)
#     for i in args:
#         print(i)
#
# my_func1(*args: 1, 2, 3)

class Human:
    def __init__(self, name= "Human" ):
         self.name = name

class Auto:
    def __init__(self, brand= "Auto" ):
        self.brand = brand
        self.passagers = []

        def add_passager(self, human):
            self.passagers.append(human)

    def add_passager(self):
        if self.passagers != []:
            print(f"В автомобілі {self.brand} зареєстровані такі пасажири ")
            for i in self.passagers:
                print(i.name)
            else:
                print("немає пасажирів")

ann = Human("Ann")
ivan = Auto("Ivan")

car = Auto("BMW")

car.add_passager(ann)
car.add_passager(ivan)

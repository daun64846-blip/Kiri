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

# class Human:
#     def __init__(self, name= "Human" ):
#          self.name = name
#
# class Auto:
#     def __init__(self, brand= "Auto" ):
#         self.brand = brand
#         self.passagers = []
#
#     def print_passager (self, human):
#             self.passagers.append(human)
#
#     def print_passager(self):
#         if self.passagers != []:
#             print(f"В автомобілі {self.brand} зареєстровані такі пасажири ")
#             for i in self.passagers:
#                 print(i.name)
#             else:
#                 print("немає пасажирів")
#
# ann = Human("Ann")
# ivan = Human("Ivan")
# car = Auto("BMW")
#
# car.print_passager(ann)
# car.print_passager(ivan)
#
# car.print_passager()

# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passenger(self):
#         if self.passengers:
#             print(f"В авто {self.brand}, зареєстровані такі пасажири:")
#             for i in self.passengers:
#                 print(i.name)
#         else:
#             print("Error 404")
#
# ann = Human("Ann")
# ivan = Human("Ivan")
# car = Auto("BMW")
#
# car.add_passenger(ann)
# car.add_passenger(ivan)
#
# car.print_passenger()

#
# class Human:
#     height = 185
#     age = 70
#
# class student(Human):
#     age = 18
#
#
#
# class worker(Human):
#     age = 45
#
#
#
# nick = student()
# taras = worker()
#  print(nick.height)
#
# print(taras.age)
# print(nick.age)

# class grandparents:
#     age = 89
#     height = 174
#     nationality = "Germany "
#
# class parents(grandparents):
#     age = 48
#
# class children(parents):
#     height = 50
#
#     def __init__(self):
#         print(self.nationality)
#         print(self.age)
#         print(self.height)
#
# nick  = children()




# class class1:
#     var = 20
#     def __init__(self):
#         self.var=10
#
#
# class class_dwar(class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# a = class_dwar()




# class grandparents:
#     def about(self):
#         print("i am grandparents")
#
#     def about_myself(self):
#             print("i am grandparents")
#
#
# class parents(grandparents):
#     def about_myself(self):
#         print("i am parents")
#
# class children(parents):
#     def __init__(self):
#         super().about()
#         super().about_myself()
#
#
# nick  = children()




# class PC:
#     def __init__(self):
#         super().__init__()
#         self.memory = 512
#
# class display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4K"
#
# class teleponia(PC, display):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
#
#
# iphone = teleponia()
# iphone.print_info()




# class AudioPlayer:
#     def play_audio(self):
#         print("Відтворюється  аудіо")
#
# class VideoPlayer:
#     def play_video(self):
#         print("Відтворюється  відео")
#
# class MultimediaPlayer(AudioPlayer, VideoPlayer):
#     def play(self):
#         print("Відтворюється мультимедійний вміст")
#
# multimedia_player = MultimediaPlayer()
#
# multimedia_player.play_audio()
# multimedia_player.play_video()
# multimedia_player.play()


class AudioPlayer:
    def __init__(self):
        super().__init__()
        print("AudioPlayer ініціалізовано.")

    def play_audio(self):
        print("Відтворюється аудіо")

class VideoPlayer:
    def __init__(self):
        super().__init__()
        print("VideoPlayer ініціалізовано")

    def play_video(self
        print("Відтворюється відео")

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def __init__(self):
        super().__init__()
        print("MultimediaPlayer ініціалізовано.")

    def play(self):
        print("Відтворюється  мультимедійний вміст")


multimedia_player = MultimediaPlayer()

multimedia_player.play_audio()
multimedia_player.play_video()
multimedia_player.play()
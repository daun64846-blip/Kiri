# try:
#     print("start code")
#     print(ещкере)
#     print("end code")
# except NameError:
#     print("Тут є помилка")
# except (NameError, ZeroDivisionError) as error:
#     print(error)

# try:
#     try:
#         print("start code")
#         print(error)
#         print("end code")
#     except NameError:
#         print("Неправильний синтаксис")
# except (NameError, ZeroDivisionError) as error:
#     print(error)

# try:
#          print("start code")
# except:
#          print("We have problem")
# else:
#          print("No problem")
# finally:
#          print("Finally")


try:
    num = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if num == 0:
        print("Помилка: Ділення на нуль неможливе.")
    else:
        result = num / num2
        print(f"Результат ділення: {result}")

    if num2 == 0:
        print("Помилка: Ділення на нуль неможливе.")
    else:
        result = num / num2
        print(f"Результат ділення: {result}")

except ValueError:
    print("Помилка: Ви ввели некоректні дані. Будь ласка, введіть число.")
def task1():
    try:
        user_input = input("Введіть число: ")
        number = int(user_input)
        print(f"Ваше число: {number}")
    except ValueError:
        print("Помилка: введене значення не можна конвертувати у число.")


def task2():
    words = ["Python", "AI", "Data", "Machine", "Learning"]

    try:
        index = int(input("Введіть індекс слова: "))
        print(f"Слово за індексом {index}: {words[index]}")
    except ValueError:
        print("Помилка: потрібно вводити тільки число.")
    except IndexError:
        print("Помилка: індекс виходить за межі списку.")


def main():
    print("Виберіть завдання:")
    print("1 – Конвертація введеного значення у число")
    print("2 – Виведення слова зі списку за індексом")

    choice = input("Ваш вибір (1 або 2): ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    else:
        print("Невірний вибір!")


if __name__ == "__main__":
    main()

import colorama
import inspect

print(dir(colorama))

print(inspect.getmembers(colorama.Fore))

from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Цей текст буде червоним")
print(Back.GREEN + "А тут зелений фон")
print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Звичайний текст")
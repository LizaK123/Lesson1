import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


print(Fore.GREEN + "Зелений текст")
print(Fore.BLUE + "Синій текст")
print(Style.BRIGHT + "Яскравий текст" + Style.RESET_ALL)
print(Back.RED + "Текст з червоним фоном")

colorama.deinit()
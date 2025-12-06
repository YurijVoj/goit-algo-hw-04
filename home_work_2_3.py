
from pathlib import Path
import sys 
from colorama import init, Fore, Back, Style
init(autoreset=True)
if len(sys.argv) > 1:
    # Перший аргумент (індекс 1) — шлях до директорії
    directory_path_str = sys.argv[1]
    # Перетворюємо рядок на об'єкт pathlib.Path
    directory_path = Path(directory_path_str)
    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.YELLOW + "Вказаний шлях не існує або не є директорією.")
        sys.exit(1)
        # Виведення переліку всіх файлів та піддиректорій
        for path in directory_path.iterdir():
            # Перевірка, чи це директорія
            if path.is_dir():
                print(Fore.RED + str(path.name))
            # Перевірка, чи це файл
            elif path.is_file():
                print(Fore.BLUE + str(path.name))
         
             




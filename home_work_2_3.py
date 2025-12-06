
import os
from pathlib import Path
import sys 
from colorama import init, Fore, Back, Style 
def process_directory(directory_path,c):
    init(autoreset=True)
    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.YELLOW + "Вказаний шлях не існує або не є директорією.")
        sys.exit(1)
    # Виведення переліку всіх файлів та піддиректорій
    for path in directory_path.iterdir():
        if path.is_file():
            print("\t"*(c+1) + Fore.BLUE + str(path.name))
        elif path.is_dir():
            print("\t"*c + Fore.RED + str(path.name) + "/")
                # Рекурсивний виклик для піддиректорії
            c+=1    
            process_directory(path, c) 
    return        
if len(sys.argv) > 1:
    # Перший аргумент (індекс 1) — шлях до директорії
        directory_path_str = sys.argv[1]
    # Перетворюємо рядок на об'єкт pathlib.Path
        directory_path = Path(directory_path_str) 
        process_directory(directory_path, c=0)      




  




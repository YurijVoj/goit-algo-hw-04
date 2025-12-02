from pathlib import Path

def total_salary(path):
    try:
        if path.exists():
            total = 0 
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.split(',')
                    if len(parts) >= 2: 
                        salary = float(parts[2])
                        total += salary                
            average_salary = total / len(file)
            my_tuple = (total, average_salary)      
            return my_tuple                
    except FileNotFoundError:   
        return print("Файл 'salary_file' не існує ") 
    except (ValueError,IOError):
                return print("Помилка при обробці файлу") 
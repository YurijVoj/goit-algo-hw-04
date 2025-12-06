from pathlib import Path

def total_salary(path):
    file_path = Path(path) 
    try:
        if file_path.exists():
            total = 0 
            number_of_lines = 0
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.split(',')
                    if len(parts) > 1: 
                        salary = float(parts[1])
                        total += salary 
                        number_of_lines += 1             
            average_salary = total / number_of_lines
            my_tuple = (total, average_salary)      
            return my_tuple                
    except FileNotFoundError:   
        return print("Файл 'salary_file' не існує ") 
    except (ValueError,IOError):
                return print("Помилка при обробці файлу") 
    
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    id = parts[0]
                    name = parts[1]
                    age = int(parts[2])
                    cats.append({'id': id, 'name': name, 'age': age})
            return cats
    except FileNotFoundError:
        print(f"Файл '{path}' не існує")
    except IOError:
        print("Помилка при обробці файлу")
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных")
        
        total_sum, incorrect_data = personal_sum(numbers)
        
        if len(numbers) == 0:
            raise ZeroDivisionError("Список пуст")
        
        return total_sum / len(numbers)
    
    except TypeError as e:
        print(e)
        return None
    except ZeroDivisionError:
        return 0

# Примеры 1: обычный список чисел
print(calculate_average([1, 2, 3, 4, 5]))  # Ожидается 3.0

# Примеры 2: список с некорректными данными
print(calculate_average([1, 2, 'a', 4]))  # Ожидается 2.3333333333333335

# Примеры 3: пустой список
print(calculate_average([]))  # Ожидается 0

# Примеры 4: не коллекция
print(calculate_average(123))  # Ожидается 'В numbers записан некорректный тип данных'
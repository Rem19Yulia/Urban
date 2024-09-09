def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            # Вызов функции и запись результата в словарь
            results[func.__name__] = func(int_list)
        except Exception as e:
            # В случае ошибки можно записать сообщение об ошибке
            results[func.__name__] = str(e)
    return results

# Пример функций для тестирования
def sum_numbers(numbers):
    return sum(numbers)

def average(numbers):
    return sum(numbers) / len(numbers)

def max_number(numbers):
    return max(numbers)

# Запуск функции apply_all_func
numbers = [1, 2, 3, 4, 5]
results = apply_all_func(numbers, sum_numbers, average, max_number)

print(results)
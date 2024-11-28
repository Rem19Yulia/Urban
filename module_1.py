# 1st program
result = 9 ** 0.5 * 5
print(result)  # Ожидаемый результат: 15.0

# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)  # Ожидаемый результат: True

# 3rd program
result1 = 2 * 2 + 2  # Без приоритета
result2 = 2 * (2 + 2)  # С приоритетом для сложения
print(result1)  
print(result2)  
print(result1 == result2)  # Ожидаемый результат: False

# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10
first_digit_after_decimal = int(shifted_number) % 10  # Получаем первую цифру после запятой
print(first_digit_after_decimal)  # Ожидаемый результат: 4

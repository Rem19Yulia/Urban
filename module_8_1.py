def add_everything_up(a, b):
    try:
        # Попробуем сложить a и b
        return a + b
    except TypeError:
        # Если возникла ошибка, то обрабатываем её
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Результат: '123.456строка'
print(add_everything_up('яблоко', 4215))    # Результат: 'яблоко4215'
print(add_everything_up(123.456, 7))        # Результат: 130.456
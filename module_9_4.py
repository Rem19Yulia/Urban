import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print("Результат сравнения:", result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything

# Пример использования:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, words):
        self.words = words

    def call(self):
        return random.choice(self.words)

words_list 
["Да", "Нет", "Может быть", "Определенно", "Не знаю"]
mystic_ball = MysticBall(words_list)

print("Случайное слово:", mystic_ball.call())

import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print("Результат сравнения:", result)

class MysticBall:
    def __init__(self, words):
        self.words = words

    def call(self):
        return random.choice(self.words)

words_list 
["Да", "Нет", "Может быть", "Определенно", "Не знаю"]
mystic_ball = MysticBall(words_list)

print("Случайное слово:", mystic_ball.call())

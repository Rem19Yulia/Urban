import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read().lower()  # Приводим текст к нижнему регистру
                    content = content.translate(str.maketrans('', '', string.punctuation))  # Убираем пунктуацию
                    words = content.split()  # Разбиваем текст на слова
                    all_words[file_name] = words  # Добавляем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден!")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Позиция начинается с 1
                result[file_name] = position
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return resultfinder = WordsFinder('Mother Goos-Monday\'s Child.txt', 'Rudyard Kipling-if.txt', 'Walt Witman - O, captain! My.txt')
print(finder.get_all_words())  # Получить все слова
print(finder.find('child'))      # Найти позицию слова 'child'
print(finder.count('if'))        # Подсчитать количество 'if'
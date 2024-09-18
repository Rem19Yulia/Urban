import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)  # Задержка 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Сначала мы вызовем функцию без потоков
start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time} секунд")

# Теперь создадим потоки
threads = []
file_data = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

start_time_threads = time.time()

for word_count, file_name in file_data:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Дожидаемся завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads} секунд")
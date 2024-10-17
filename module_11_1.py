#рассмотрю три библиотеки

#1. requests — для работы с HTTP-запросами.
#2. pandas — для анализа данных.
#3. matplotlib — для визуализации данных.

#1. Requests

#Библиотека requests упрощает процесс работы с HTTP-запросами. Она позволяет отправлять GET, POST и другие типы запросов, а также обрабатывать ответы.

#Пример использования:

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()
print(data)


#Возможности: Отправка различных типов HTTP-запросов; Обработка JSON-ответов; Управление параметрами запросов и заголовками.

#2. Pandas

#Pandas — это мощная библиотека для анализа и манипуляции данными. Она поддерживает структуры данных, такие как DataFrame и Series.

#Пример использования:

import pandas as pd

# Чтение данных из CSV-файла
data = pd.read_csv('data.csv')
print(data.head())

# Простой анализ
summary = data.describe()
print(summary)


#Возможности:Чтение и запись данных в различных форматах (CSV, Excel, SQL);Простой анализ и агрегация данных;Фильтрация и манипуляция данными.

#3. Matplotlib

#Библиотека matplotlib позволяет визуализировать данные с помощью графиков, диаграмм и других визуальных инструментов.

#Пример использования:

import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Создание графика
plt.plot(x, y)
plt.title('Простой график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


#Возможности:Построение различных типов графиков и диаграмм; Настройка внешнего вида графиков (цвета, метки, легенды); Сохранение графиков в различных форматах (PNG, PDF).

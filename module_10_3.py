import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:  # Блокировка для безопасного доступа к balance
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

            time.sleep(0.001)  # Имитация скорости выполнения пополнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")

            with self.lock:  # Блокировка для безопасного доступа к balance
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств.")

            time.sleep(0.001)  # Имитация скорости выполнения снятия


# Создание объекта банка
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Итоговый баланс
print(f"Итоговый баланс: {bk.balance}")
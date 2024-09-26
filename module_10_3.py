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

                # Если баланс больше или равен 500 и замок заблокирован, разблокируем его
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

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
                    self.lock.acquire()  # Блокировка потока

            time.sleep(0.001)  # Имитация скорости выполнения снятия


# Создание объекта банка
bank = Bank()

# Создание потоков для методов deposit и take
deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

# Запуск потоков
deposit_thread.start()
take_thread.start()

# Ожидание завершения потоков
deposit_thread.join()
take_thread.join()

# Итоговый баланс
print(f"Итоговый баланс: {bank.balance}")
class Runner:
    def __init__(self, name, speed=5):  # Исправлено на __init__
        if not isinstance(name, str):
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.name = name
        self.distance = 0
        if speed <= 0:
            raise ValueError(f'Скорость не может быть отрицательной или нулевой, сейчас {speed}')
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):  # Исправлено на __str__
        return self.name

    def __repr__(self):  # Исправлено на __repr__
        return self.name

    def __eq__(self, other):  # Исправлено на __eq__
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):  # Исправлено на __init__
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers










import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest:
    def test_walk(self):
        try:
            runner = Runner('Тест', -5)  # Передаем отрицательное значение
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем не строку
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info('"test_run" выполнен успешно')

# Пример запуска тестов
runner_test = RunnerTest()
runner_test.test_walk()
runner_test.test_run()
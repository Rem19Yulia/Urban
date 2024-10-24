import unittest

def skip_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f'Тест {func.__name__} в этом кейсе заморожен')
            return
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_example_1(self):
        self.assertTrue(True)  # Ваше тестовое условие

    @skip_frozen
    def test_example_2(self):
        self.assertEqual(1, 1)  # Ваше тестовое условие

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_frozen
    def test_example_1(self):
        self.assertTrue(False)  # Ваше тестовое условие

    @skip_frozen
    def test_example_2(self):
        self.assertEqual(2, 2)  # Ваше тестовое условие
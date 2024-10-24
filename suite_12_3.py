import unittest
from Tests_12_3 import RunnerTest, TournamentTest

# Создаем класс TestSuite
class MyTestSuite(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.makeSuite(RunnerTest))
        self.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект класса TextTestRunner
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = MyTestSuite()
    runner.run(suite)
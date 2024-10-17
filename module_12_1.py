import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Бегун 1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Бегун 2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Бегун 3")
        runner2 = Runner("Бегун 4")
        
        for _ in range(10):
            runner1.run()
            runner2.walk()
        
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
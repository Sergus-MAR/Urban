import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_walk_obj = Runner('Ivan')
        for i in range(10):
            test_walk_obj.walk()
        self.assertEqual(test_walk_obj.distance, 50)

    def test_run(self):
        test_run_obj = Runner('Fedor')
        for i in range(10):
            test_run_obj.run()
        self.assertEqual(test_run_obj.distance, 100)

    def test_challenge(self):
        test_challenge_obj_1 = Runner('Max')
        test_challenge_obj_2 = Runner('Alex')
        for i in range(10):
            test_challenge_obj_1.run()
            test_challenge_obj_2.walk()
        self.assertNotEqual(test_challenge_obj_1.distance, test_challenge_obj_2.distance)


if __name__ == "__main__":
    unittest.main()

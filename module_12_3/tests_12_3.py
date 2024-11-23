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

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_walk_obj = Runner('Ivan')
        for i in range(10):
            test_walk_obj.walk()
        self.assertEqual(test_walk_obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run_obj = Runner('Fedor')
        for i in range(10):
            test_run_obj.run()
        self.assertEqual(test_run_obj.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_challenge_obj_1 = Runner('Max')
        test_challenge_obj_2 = Runner('Alex')
        for i in range(10):
            test_challenge_obj_1.run()
            test_challenge_obj_2.walk()
        self.assertNotEqual(test_challenge_obj_1.distance, test_challenge_obj_2.distance)

class Runner_:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
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


class TournamentTest(unittest.TestCase):
    
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(self.all_results[0][2] == self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(self.all_results[1][2] == self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_3.start())
        self.assertTrue(self.all_results[2][3] == self.runner_3.name)

    @classmethod
    def tearDownClass(cls):
        resaulting_dict = {}
        for dict_element in TournamentTest.all_results:
            for key, val in dict_element.items():
                resaulting_dict[key] = val.name
            print(resaulting_dict)


if __name__ == "__main__":
    unittest.main()
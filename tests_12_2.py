import unittest

class Runner:
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
    
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)


    def test_tournament_1(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(self.all_results[0][2] == self.runner_3.name)
    def test_tournament_2(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(self.all_results[1][2] == self.runner_3.name)
    def test_tournament_3(self):    
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
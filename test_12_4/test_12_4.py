import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info(f'"test_walk" выполнен успешно')
            runner_1 = Runner('Mark', speed=-20)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            logging.info(f'"test_run" выполнен успешно')
            runner_2 = Runner(name=77)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    unittest.main()

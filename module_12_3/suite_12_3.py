import unittest
from tests_12_3 import RunnerTest, TournamentTest

some_unit_test = unittest.TestSuite()
all_tests = [unittest.TestLoader().loadTestsFromTestCase(RunnerTest),
             unittest.TestLoader().loadTestsFromTestCase(TournamentTest)]
some_unit_test.addTests(all_tests)

test_12_3 = unittest.TextTestRunner(verbosity=2) #verbosity=2 - вывод с подробной информацией 
test_12_3.run(some_unit_test)

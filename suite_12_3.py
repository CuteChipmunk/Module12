import unittest
import Homework12_2
import Homework12_1

my_case = unittest.TestSuite()

my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(Homework12_2.TournamentTest))
my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(Homework12_1.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_case)
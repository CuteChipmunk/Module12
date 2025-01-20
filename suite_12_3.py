import unittest
import tests12_3

my_case = unittest.TestSuite()

my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.TournamentTest))
my_case.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_case)

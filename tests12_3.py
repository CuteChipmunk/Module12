import unittest
import runner
import runner_and_tournament as run

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = runner.Runner('Rick')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = runner.Runner('KAte')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance,100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = runner.Runner('Mike')
        runner_4 = runner.Runner('Lisa')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self. assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = run.Runner('Усэйн', 10)
        self.runner_2 = run.Runner('Андрей', 9)
        self.runner_3 = run.Runner('Ник', 3)
        self.runner_4 = run.Runner('Алекс', 5)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            print(f'TEST: {testkey}')
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        runner_1 = run.Tournament(90, self.runner_1, self.runner_3)
        finish = runner_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runner_3))
        self.all_results[f'Результат {self.runner_1} и {self.runner_3}'] = finish

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        runner_1 = run.Tournament(90, self.runner_2, self.runner_3)
        finish = runner_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runner_3))
        self.all_results[f'Результат {self.runner_2} и {self.runner_3}'] = finish

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        runner_1 = run.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        finish = runner_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runner_3))
        self.all_results[f'Результат {self.runner_1}, {self.runner_2} и {self.runner_3}'] = finish

if __name__ == '__main__':
    unittest.main()
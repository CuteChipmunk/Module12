import logging
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w+', filename='runner_tests.log',
                    encoding='utf=8', format='%(asctime)s | %(levelname)s | %(message)s')

class Test_1(unittest.TestCase):
    def test_walk(self):
        try:
            walker = Runner("mike", -3)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.INFO('test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner - Runner(6, 15)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 50)
            logging.INFO('Успех')
        except:
            logging.warning('Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    unittest.main()
import unittest
import runner

"""Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.
Пример результата выполнения программы:
Вывод на консоль:
Ran 3 tests in 0.001s OK

Примечания:
Попробуйте поменять значения в одном из тестов, результаты"""

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner('Rick')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('KAte')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance,100)

    def test_challenge(self):
        runner_3 = runner.Runner('Mike')
        runner_4 = runner.Runner('Lisa')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self. assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == '__main__':
    unittest.main()



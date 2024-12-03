import logging
import unittest
from modul_12_4 import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            name = Runner('Кристина', -5)
            for i in range(10):
                name.walk()
            self.assertEqual(name.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            name_1 = Runner(15)
            for i in range(10):
                name_1.run()
            self.assertEqual(name_1.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == "__main__":
    unittest.main()




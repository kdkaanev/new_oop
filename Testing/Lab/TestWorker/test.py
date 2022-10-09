


from TestWorker.worker import Worker
import unittest

class WorkerTest(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 2
    MONEY = 0
    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init__corect_name_salary_energy(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest__expect_energy_increment(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_work__when_energy_is_0__espect_to_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
            self.assertIsNone(ex)

    def test_work__when_enougt_energy__money_in_salary_raise(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test_work__espect_decrease_energy(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_get_info__espect_proper_string(self):
        self.worker.get_info()
        result = f'{self.worker.name} has saved {self.worker.money} money.'
        espected = f'{self.NAME} has saved {0} money.'
        self.assertEqual(result, espected)


if __name__ == '__main__':
    unittest.main()







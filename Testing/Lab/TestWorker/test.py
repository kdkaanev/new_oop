
import unittest

from TestWorker.worker import Worker

'''
	

•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values

'''
class WorkerTest(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 1
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

    def test_work__when_enougt_energy__money_in_salary_raise(self):
        pass







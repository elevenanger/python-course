import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.vince = Employee('vince', 'carter', 2000)

    def test_give_default_raise(self):
        self.vince.give_raise()
        self.assertEqual(self.vince.salary, 7000)

    def test_give_custom_raise(self):
        self.vince.give_raise(1000)
        self.assertTrue(self.vince.salary == 3000)


if __name__ == '__main__':
    unittest.main()

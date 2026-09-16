

import unittest
# from calculator import run_operation
import calculator

class TestCalculations(unittest.TestCase):
  def __init__(self, methodName = "runTest"):
    super().__init__(methodName)
  def test_one_plus_two(self):
      assert calculator.run_operation(1,"+",2) == 3
  def test_one_plus_two_does_not_equal_four(self):
      assert calculator.run_operation(1,"+",2) != 4
  def test_one_plus_two_is__integer(self):
      assert isinstance(calculator.run_operation(1,"+",2), int)
  def test_subtraction(self):
      assert calculator.run_operation(3,"-",2) == 1
  def test_multiplication(self):
      assert calculator.run_operation(3,"*",5) == 15
  def test_division(self):
      assert calculator.run_operation(10,"/",2) == 5



if __name__ == '__main__':
    unittest.main(verbosity=3)
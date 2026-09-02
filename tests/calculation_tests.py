

import unittest
# from calculator import run_operation
from calculator import calculator

class TestCalculations(unittest.TestCase):
  def __init__(self, methodName = "runTest"):
    super().__init__(methodName)
  def test_one_plus_two():
      assert calculator.run_operation(1,"+",2) == 3


if __name__ == '__main__':
    unittest.main(verbosity=2)
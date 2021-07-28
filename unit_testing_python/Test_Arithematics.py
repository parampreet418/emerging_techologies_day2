import calculate
import unittest
import UnitTest_Arithmetics



class Test_Arithmetics:
    # Default module basic Unit Testing
    def run_test(self):
        calc = calculate.Arithematics()
        assert calc.sum(2,2) == 4
        assert calc.sub(5, 2) == 3
        assert calc.sub(5, 2) != 2
        assert calc.multiply(3, 2) == 6
        # assert calc.div(4, 2) == 4
        # assert calc.mod(5, 2) == 2

        assert calc.sub(5, 2) <= 3
       # assert calc.sub(5, 2) > 3

     #unit test module Unit Testing
  #  def test_unit_example(self):
     #  assert
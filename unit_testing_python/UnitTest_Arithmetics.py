import calculate
import unittest

class UnitTest_Arithmetics(unittest.TestCase):
    # Default module basic Unit Testing
    def run_test(self):
        arithematics = calculate.Arithematics()

        self.assertAlmostEqual(arithematics.sum(2,2),4)
       # assert arithematics.sum(2,2) == 4
       #  assert arithematics.sub(5, 2) == 3
        self.assertAlmostEqual(arithematics.sub(5,2),3)
       # assert arithematics.sub(5, 2) != 2
        self.assertNotAlmostEqual(arithematics.sub(5,2),2)


       # assert calculate.multiply(3, 2) == 6
        self.assertAlmostEqual(arithematics.multiply(3,2),6)

       # assert calculate.div(4, 2) == 4
       # assert calculate.mod(5, 2) == 2

       # assert calculate.sub(5, 2) <= 3
       #  assert calculate.sub(5, 2) > 3
        self.assertGreaterEqual(arithematics.sub(5,2),3)
       # assert calculate.sub(5, 2) == 3  fail
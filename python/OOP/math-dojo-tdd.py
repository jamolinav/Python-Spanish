import unittest

class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
    	# tu código aquí
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
    	# tu código aquí
        self.result -= num
        for i in nums:
            self.result -= i
        return self

class pruebas(unittest.TestCase):
    def test1(self):
        self.assertEqual(self.math.add(2).add(2,5,1).subtract(3,2).result, 5)

    def setUp(self):
        self.math = MathDojo()

if __name__ == '__main__':
    unittest.main()


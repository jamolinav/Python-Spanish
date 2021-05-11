import unittest

def reverseList(arr):
    arr.reverse()
    return arr

def isPalindrome(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

def monedas(monto):
    moneda25 = round(monto / 25)
    resto = monto % 25
    moneda10 = round(resto / 10)
    resto = resto % 10
    moneda5 = round(resto / 5)
    resto = resto % 5
    return [moneda25,moneda10,moneda5,resto]

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

class pruebas(unittest.TestCase):
    def test1ReverseList(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])

    def test2ReverseList(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])

    def test3IsPalindrome(self):
        self.assertEqual(isPalindrome('somos'), True)

    def test4Monedas(self):
        self.assertEqual(monedas(87), [3, 1, 0, 2])

    def test5Factorial(self):
        self.assertEqual(factorial(5), 12)

if __name__ == '__main__':
    unittest.main()
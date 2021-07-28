import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('param'.upper(), 'PARAM')

    def test_isupper(self):
        self.assertTrue('PARAM'.isupper())
        self.assertFalse('Param'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['Parampreet', 'Kaur'])

        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
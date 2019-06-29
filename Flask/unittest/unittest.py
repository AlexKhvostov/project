import unittest


class TestDivision(unittest.TestCase):

  def test_integer_division(self):
      self.assertIs(10 / 5, 2.0)


if __name__ == '__main__':
    unittest.main()
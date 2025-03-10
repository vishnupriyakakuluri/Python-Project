from dee import dee as d
import unittest
class TestSum(unittest.TestCase):
       def test_sum(self):
              self.assertEqual(d.add(1,5), 15, "wrong")
if __name__ == '__main__':
       unittest.main()
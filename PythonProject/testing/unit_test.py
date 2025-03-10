# #unit testing
# #Don't give print, just as it is
# assert sum([1, 2, 3]) == 6
# #This will not output anything because the values are correct.
# #change the value show the error
# --------------------------
# def test_sum():
#        assert sum([1, 2, 3]) == 6, "Should be 6"
# #2nd step with tuple to show error
# def test_sum_tuple():
#        assert sum((1, 2, 2)) == 6, "Should be 6"
# if __name__ == "__main__":
#        test_sum()
#        test_sum_tuple()
#        print("Everything passed")
#
# ----------------------------------
# #Actual one with class
# import unittest
# class TestSum(unittest.TestCase):
#        def test_sum(self):
#               self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
#        def test_sum_tuple(self):
#               self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
# if __name__ == '__main__':
#        unittest.main()
# ---------------------------------------------
#actual unit testing

# import unittest
# def sum(a,b):
#     return a+b
# class dee(unittest.TestCase):
#     def test_ab(self):
#
#         a, b = 10, 5
#         result = sum(a, b)
#         self.assertEqual(result, 10+5)
#         print('hghh')
#
# if __name__=='__main__':
#     unittest.main()
# ..........................................
# #more ex
# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('dee'.upper(), 'DEE')
#
#     def test_isupper(self):
#         self.assertTrue('DEE'.isupper())
#         self.assertFalse('DEE'.islower())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()
# -------------------------------------------------
# #create a module and try
# -----------------------------
# # for the same program type in Terminal
# python -m unittest day2(filename)
# ----------------------------------
# #if single file is there in folder, need not to give file name but let it discover
# python -m unittest discover
# --------------------------------

import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print('\n------------------------------ start ------------------------------')
        pass

    def test_1(self):
        print(11/4)
        print(11//4)

    def test_2(self):
        print('2')

    def test_3(self):
        print('3')

    def test_4(self):
        print('4')

    def tearDown(self):
        print('------------------------------  end  ------------------------------')
        pass

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(Test)
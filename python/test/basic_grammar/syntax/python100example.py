import unittest

'''
    [快速入门（完整）：Python实例100个（基于最新Python3.7版本）](https://blog.csdn.net/weixin_41084236/article/details/81564963)
'''

class Test(unittest.TestCase):

    def setUp(self):
        print('\n------------------------------ start ------------------------------')
        pass

    def test_1(self):
        print('1')

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
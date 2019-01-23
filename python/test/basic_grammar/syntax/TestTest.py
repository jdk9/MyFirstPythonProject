import unittest
'''
    测试类
'''
class TestTest(unittest.TestCase):
    def setUp(self):
        print('------------------------------ start ------------------------------')
        pass

    '''
        == 和 is 的区别
        
        Python中对象包含的三个基本要素, 分别是: id(身份标识), type(数据类型)和value(值)
        is和==都是对对象进行比较判断作用的, 但对对象比较判断的内容并不相同下面来看看具体区别在哪
        == 比较操作符和is同一性运算符区别, 是python标准操作符中的比较操作符, 用来比较判断两个对象的value(值)是否相等
        is 也被叫做同一性运算符, 这个运算符比较判断的是对象间的唯一身份标识, 也就是id是否相同
    '''
    def test_1(self):
        # 只有数值型, 字符串型和tuple型的情况下, a is b才为True, 当a和b是list, dict或set型时, a is b为False
        # 简言之: id()相同is为True, value相同==为True
        a = 31415926535897932384626433832795028841971693993751058209749445903078164862089986280
        b = 31415926535897932384626433832795028841971693993751058209749445903078164862089986280
        self.test_1_print(a, b)
        a = 'adc'
        b = 'adc'
        self.test_1_print(a, b)
        a = ((1, 2, 3), (1, 2, 3))
        b = ((1, 2, 3), (1, 2, 3))
        self.test_1_print(a, b)
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.test_1_print(a, b)
        a = {'name':'name', 'age':22}
        b = {'name':'name', 'age':22}
        self.test_1_print(a, b)
        a = {1, 2, 3}
        b = {1, 2, 3}
        self.test_1_print(a, b)

    def test_1_print(self, a, b):
        print('%s\t\'a == b\' = %s\t a = %s' % (type(a), (a == b), a))
        print('%s\t\'a is b\' = %s' % (type(a), (a is b)))

    def test_2(self):
        a = 1
        print(type(a))

    def tearDown(self):
        print('------------------------------  end  ------------------------------')
        pass




if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestTest)
    # unittest.main()
import unittest
'''
    [Python 3 教程](http://www.runoob.com/python3/python3-tutorial.html)
'''
class W3School(unittest.TestCase):

    def setUp(self):
        print('\n------------------------------ start ------------------------------')



    '''
        Python 3 教程
    '''
    # 查看python版本
    def test_11(self):
        import os
        cmd = 'python -V'
        p = os.popen(cmd)
        print(p.read())
        # cmd = 'exit'
        # p = os.popen(cmd)
        # print(p.read())

    # 第一个Python3.x程序
    def test_12(self):
        print('Hello World!')



    '''
        Python3 基础语法
    '''
    # 编码
    """
        # -*- coding: utf-8 -*-
    """

    # 标识符
    def test_21(self):
        你好6 = '666'
        print(你好6)

    # python保留字
    def test_22(self):
        import keyword
        print(keyword.kwlist)

    # 注释

    # 行与缩进

    # 多行语句
    def test_23(self):
        str = '1' + \
              '2'

    # 数字(Number)类型
    def test_23(self):
        int_tmp = 1
        bool_tmp = True
        float_tmp = 1.0
        complex_tmp = 1 + 5.6j
        print(int_tmp)
        print(bool_tmp)
        print(float_tmp)
        print(complex_tmp)

    # 字符串(String)
    def test_24(self):
        word = 'hello'
        sentence = 'hello world!'
        paragraph = '''nice!
        hello world!
        '''

        str = '0123456789'
        print(str)
        print(str[3])
        print(str[3:5])
        print(str[3:-1])
        print(str[3:])
        print(str * 2)
        print(str + 'gg')

        print('hello\tworld!')
        print(r'hello\tworld!')

    # 空行

    # 等待用户输入
    def test_25(self):
        input("按下 Enter 键后退出.")

    # 同一行显示多条语句
    def test_26(self):
        import sys; x = 'runoob'; sys.stdout.write(x + '666') ; print()










    def test(self):
        print('>>')
        print(123, end='666')
        print('<<')
        print('>>')
        print(1, 2, 3, end='666', sep='_')
        print('<<')

    def tearDown(self):
        print('------------------------------  end  ------------------------------')

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(W3School)
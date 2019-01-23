import unittest
'''
    # 运算符, 优先级从低到高
'''
class TestOperator(unittest.TestCase):
    def setUp(self):
        print('\n------------------------------ start ------------------------------')
        pass

    # lambda表达式
    def test_1(self):
        # print('\'\'\t= %s' % ());
        # TODO - 什么是lambda表达式
        pass

    # 布尔: 或, 与, 非
    def test_2(self):
        print('True or False = %s' % (True or False))
        print('True and False = %s' % (True and False))
        print('not False = %s' % (not False))
        print('' % (not False))
        pass

    # 测试: in, not in ->
    #      is, not is ->
    def test_3(self):
        print('\'1 in [1, 2, 3, 4]\'\t= %s' % (1 in [1, 2, 3, 4]));
        print('\'5 in [1, 2, 3, 4]\'\t= %s' % (5 in [1, 2, 3, 4]));
        print('\'1 not in [1, 2, 3, 4]\'\t= %s' % (1 not in [1, 2, 3, 4]));
        pass

    # 比较: <, <=, >, >=, !=, ==
    def test_4(self):
        pass

    # 按位: 或, 亦或, 与
    def test_5(self):

        pass

    # 移位: <<, >>
    def test_6(self):
        pass

    # 加+, 减-, 乘*, 除/, 取余%
    def test_7(self):
        pass

    # 正负号
    def test_8(self):
        pass

    # 按位翻转
    def test_9(self):
        pass

    # 指数
    def test_10(self):
        pass

    # 属性参考
    def test_11(self):
        pass

    # 下标
    def test_12(self):
        pass

    # 寻址段
    def test_13(self):
        pass

    # 函数调用
    def test_14(self):
        pass

    # 绑定或元祖显示
    def test_15(self):
        pass
    pass

    # 列表显示
    def test_16(self):
        pass
    pass

    # 字典显示
    def test_17(self):
        pass
    pass

    # 字符串转换
    def test_18(self):
        pass
    pass

    def tearDown(self):
        print('------------------------------  end  ------------------------------')
        pass

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestOperator)
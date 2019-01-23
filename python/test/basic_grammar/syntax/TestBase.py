import unittest
'''
    1. python中数有四种类型: 整数, 长整数, 浮点数和复数.
    2. 字符串（字符的序列
    3. 标识符的命名
    4. python程序中用到的任何"东西"都成为"对象"
    5. 逻辑行和物理行
    6. 缩进
    7. 空类型和空语句
'''
class TestBase(unittest.TestCase):
    def setUp(self):
        print('\n------------------------------ start ------------------------------')
        pass

    # 1. python中数有四种类型：整数, 长整数, 浮点数和复数.
    def test_1(self):
        # 整数
        print(1)
        # 长整数
        print(1111111111111111111111111111111)
        # 浮点数
        print(1.23)
        print(1.23e-8)
        # 负数
        print(1+5j)
        print(complex(1, 5))
        print(1.5+5.5j)

    # 2. 字符串（字符的序列）
    def test_2(self):
        # 单引号和双引号不区分
        print('hello')
        print("world")
        # 多行文本 -> 连续三个引号
        print('''1
2
3''')
        # 转移符 -> '\'
        print('a\tb\nc')
        # 自然字符串 -> 前缀r或R
        print(r'a\tb\nc')
        # unicode字符串 -> 前缀u或U
        print(u'this is an unicode string.')
        # 字符串是不可变的

        # 按字面意义级联字符串
        print('this' 'is' 'string')

    # 3. 标识符的命名
    def test_3(self):
        # 第一个字符必须是字母或下划线
        # 标识符的其他的部分由字母, 数字和下划线组成
        _1 = '1'
        a = _1
        print(a)
        # 标识符对大小写敏感
        A = '2'
        print(A)

    # 4. python程序中用到的任何"东西"都成为"对象"

    # 5. 逻辑行和物理行
    def test_4(self):
        # 分号表示一个逻辑行的结束, 但是实际中一般每个物理行只写一个逻辑行, 可以避免使用分号
        a = 1; b = a
        # 多个物理行中可以写一个逻辑行, \的使用被称为'明确的行连接'
        s = 'this \
is s string'
        print\
            (s);

    # 6. 缩进
    '''
        空白在python是非常重要的, 行首的空白是最重要的, 又称为缩进.
        行首的空白(空格和制表符)用来决定逻辑行的缩进层次, 从而决定语句分组.
        这意味着同一层次的语句必须有相同的缩进, 每一组这样的语句称为一个块.
    　　注意：不要混合使用空格和制表符来缩进, 因为在跨越不同的平台时无法正常工作.
    '''

    # 7. 空类型和空语句
    def test_5(self):
        print(None)
        pass

    def tearDown(self):
        print('------------------------------  end  ------------------------------')
        pass

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestBase)
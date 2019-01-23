# 1. 导入模块
import unittest
'''
    原文链接: [unittest.TestCase中测试用例执行顺序问题](http://blog.sina.com.cn/s/blog_68f262210102v6jv.html)
    参考链接
        1. [python接口自动化测试(六)-unittest-单个用例管理](https://www.cnblogs.com/puresoul/p/7490528.html)
'''
# 2. 继承自unittest.TestCase类 (好像这个类名必须是以Test开头的, 还不能就是Test, 后面必须有字符)
class Test_2019114_172341(unittest.TestCase):

    # 3. 配置环境：进行测试前的初始化工作
    def setUp(self):
        print('\n------------------------------ start ------------------------------')
        pass

    # 4. 定义测试用例, 名字以“test”开头
    def test_a(self):
        print('a')
        # # 5. 定义assert断言, 判断测试结果
        # self.assertEqual(a, b)

    def test_b(self):
        print('b')

    def test_c(self):
        print('c')

    def test_d(self):
        print('d')
    
    # 6. 清理环境
    def tearDown(self):
        print('------------------------------  end  ------------------------------')
        pass

if __name__ == '__main__':
    '''
        7. 使用说明
            [1]. 仅执行单个方法 -> 选中某个方法名称所在行(方法体长的在方法中也可以), Ctrl+Shift+F10执行
            [2]. 执行全部方法   -> 除上述位置随便放置光标即可执行全部方法
    '''
    unittest.TestLoader().loadTestsFromTestCase(Test_2019114_172341)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    '''
        # 7. 该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
        unittest.main()
    '''
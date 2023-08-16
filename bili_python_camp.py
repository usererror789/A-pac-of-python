#unittest 检查bug,在单元测试文件中import要测试的对象，在unittest.TestCase类下创建子类class MyTestCase(unittest.TestCase)
#定义类测试属性，注意命名要以test_开头。在self.assertEqual(a,b)输入a：测试对象，b:预期结果。在终端输入 python -m unittest 运行即可
"""
class Shopping_list:
    '''shoppinglist输入字典'''

    def __init__(self,shoppinglist):
        self.shoppinglist = shoppinglist

    def get_item_count(self):
        return len(self.shoppinglist)

    def get_item_price(self):
        total_price = 0
        for price in self.shoppinglist.values():
            total_price += price
        return total_price
"""
'''以下为测试代码'''
"""
import unittest
from bili_python_camp import Shopping_list

class TestShoppinglist(unittest.TestCase):
'''创建测试类TestShoppinglist'''

    def setUp(self):
        self.shoppinglist = Shopping_list({"帽子": 30, "牙刷": 5, "拖鞋": 15})
'''使用setUp语句将初始类Shopping_list(shoppinglist)属性绑定至测试类中的self.shoppinglist,避免方法中冗余引用'''

    def test_get_item_count(self):
        self.assertEqual(self.shoppinglist.get_item_count(),3)
'''测试get_item_count()方法'''

    def test_get_item_price(self):
        self.assertEqual(self.shoppinglist.get_item_price(),50)
'''测试get_item_price()方法'''

if __name__ == '__main__':
    unittest.main()
"""
#类似的，assertEqual(A,B),assertTure(A),assertIn(A,B),assertNotEqual(A,B),assertFalse(A),assertNotIn(A,B)



#高阶函数：把函数当做参数传入另一个函数
"""
'''定义简单函数'''
def calculate_square(num):
    return num * num
def calculate_plus10(num):
    return num + 10
def print_with_vertical_bar(num,result):
    print(f'''
    |数字参数|{num}
    |计算结果|{result}''')
'''定义高阶函数，高阶函数的参数calculator是作为输入函数名的参数。区分 函数名() 和 函数名 的区别，前者调用函数返回值，后者代表函数'''
def calculate_and_print(num,calculator,formater):
    result = calculator(num)
    formater(num,result)

calculate_and_print(3,calculate_square,print_with_vertical_bar)

calculate_and_print(3,calculate_plus10,print_with_vertical_bar)


##匿名函数 lambda：简单函数的一种定义方法

calculate_and_print(7,lambda num:num * num,print_with_vertical_bar)
"""



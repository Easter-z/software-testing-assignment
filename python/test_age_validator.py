import unittest
from age_validator import AgeValidator

class TestAgeValidator(unittest.TestCase):
    
    def test_is_valid_age_boundary_values(self):
        # 边界值测试
        self.assertFalse(AgeValidator.is_valid_age(17))  # 下边界外
        self.assertTrue(AgeValidator.is_valid_age(18))   # 下边界
        self.assertTrue(AgeValidator.is_valid_age(19))   # 下边界内
        
        self.assertTrue(AgeValidator.is_valid_age(64))   # 上边界内
        self.assertTrue(AgeValidator.is_valid_age(65))   # 上边界
        self.assertFalse(AgeValidator.is_valid_age(66))  # 上边界外
    
    def test_is_valid_age_equivalence_classes(self):
        # 等价类测试 - 有效等价类
        self.assertTrue(AgeValidator.is_valid_age(25))   # 有效类中间值
        self.assertTrue(AgeValidator.is_valid_age(45))   # 有效类中间值
        self.assertTrue(AgeValidator.is_valid_age(60))   # 有效类中间值
        
        # 等价类测试 - 无效等价类
        self.assertFalse(AgeValidator.is_valid_age(0))   # 远小于下边界
        self.assertFalse(AgeValidator.is_valid_age(10))  # 小于下边界
        self.assertFalse(AgeValidator.is_valid_age(100)) # 远大于上边界
    
    def test_is_valid_age_invalid_input(self):
        with self.assertRaises(TypeError):
            AgeValidator.is_valid_age("18")
        with self.assertRaises(TypeError):
            AgeValidator.is_valid_age(18.5)
    
    def test_get_age_category_equivalence_classes(self):
        # 无效等价类
        self.assertEqual(AgeValidator.get_age_category(17), "无效年龄")
        self.assertEqual(AgeValidator.get_age_category(66), "无效年龄")
        
        # 有效等价类 - 青年
        self.assertEqual(AgeValidator.get_age_category(18), "青年")
        self.assertEqual(AgeValidator.get_age_category(25), "青年")
        self.assertEqual(AgeValidator.get_age_category(35), "青年")
        
        # 有效等价类 - 中年
        self.assertEqual(AgeValidator.get_age_category(36), "中年")
        self.assertEqual(AgeValidator.get_age_category(45), "中年")
        self.assertEqual(AgeValidator.get_age_category(50), "中年")
        
        # 有效等价类 - 中老年
        self.assertEqual(AgeValidator.get_age_category(51), "中老年")
        self.assertEqual(AgeValidator.get_age_category(60), "中老年")
        self.assertEqual(AgeValidator.get_age_category(65), "中老年")
    
    def test_get_age_category_boundary_values(self):
        # 边界值测试
        self.assertEqual(AgeValidator.get_age_category(17), "无效年龄")
        self.assertEqual(AgeValidator.get_age_category(18), "青年")
        self.assertEqual(AgeValidator.get_age_category(35), "青年")
        self.assertEqual(AgeValidator.get_age_category(36), "中年")
        self.assertEqual(AgeValidator.get_age_category(50), "中年")
        self.assertEqual(AgeValidator.get_age_category(51), "中老年")
        self.assertEqual(AgeValidator.get_age_category(65), "中老年")
        self.assertEqual(AgeValidator.get_age_category(66), "无效年龄")

if __name__ == '__main__':
    unittest.main()

import pytest
from palindrome import is_palindrome, is_palindrome_simple


class TestPalindrome:
    """测试 is_palindrome 函数"""
    
    def test_valid_palindrome(self):
        """测试有效的回文字符串"""
        assert is_palindrome("A man a plan a canal Panama") == True
        assert is_palindrome("racecar") == True
        assert is_palindrome("12321") == True
    
    def test_non_palindrome(self):
        """测试非回文字符串"""
        assert is_palindrome("hello") == False
        assert is_palindrome("python") == False
        assert is_palindrome("12345") == False
    
    def test_case_insensitive(self):
        """测试大小写不敏感"""
        assert is_palindrome("Racecar") == True
        assert is_palindrome("MaDaM") == True
    
    def test_with_special_chars(self):
        """测试包含特殊字符的回文"""
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("race car") == True
        assert is_palindrome("Was it a car or a cat I saw?") == True
    
    def test_empty_and_whitespace(self):
        """测试空字符串和空白字符串"""
        assert is_palindrome("") == False
        assert is_palindrome("   ") == False
        assert is_palindrome("  a  ") == True
    
    def test_single_character(self):
        """测试单字符"""
        assert is_palindrome("a") == True
        assert is_palindrome("1") == True
    
    def test_invalid_input_type(self):
        """测试无效输入类型"""
        with pytest.raises(TypeError):
            is_palindrome(123)
        with pytest.raises(TypeError):
            is_palindrome([1, 2, 1])
        with pytest.raises(TypeError):
            is_palindrome(None)


class TestPalindromeSimple:
    """测试 is_palindrome_simple 函数"""
    
    def test_simple_palindrome(self):
        """测试简单回文"""
        assert is_palindrome_simple("aba") == True
        assert is_palindrome_simple("12321") == True
    
    def test_simple_non_palindrome(self):
        """测试简单非回文"""
        assert is_palindrome_simple("abc") == False
        assert is_palindrome_simple("12345") == False
    
    def test_empty_string(self):
        """测试空字符串"""
        assert is_palindrome_simple("") == False


def test_both_functions_consistency():
    """测试两个函数在简单情况下的结果一致性"""
    test_cases = ["racecar", "hello", "12321", "abcba"]
    
    for case in test_cases:
        # 对于不包含特殊字符的字符串，两个函数结果应该一致
        assert is_palindrome(case) == is_palindrome_simple(case)

import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    
    def test_reverse_string(self):
        self.assertEqual(StringUtils.reverse_string("hello"), "olleh")
        self.assertEqual(StringUtils.reverse_string(""), "")
        self.assertEqual(StringUtils.reverse_string("a"), "a")
        self.assertEqual(StringUtils.reverse_string("123"), "321")
    
    def test_reverse_string_invalid_input(self):
        with self.assertRaises(TypeError):
            StringUtils.reverse_string(123)
        with self.assertRaises(TypeError):
            StringUtils.reverse_string(None)
    
    def test_is_palindrome(self):
        self.assertTrue(StringUtils.is_palindrome("racecar"))
        self.assertTrue(StringUtils.is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(StringUtils.is_palindrome("hello"))
        self.assertTrue(StringUtils.is_palindrome(""))
        self.assertTrue(StringUtils.is_palindrome("a"))
    
    def test_count_vowels(self):
        self.assertEqual(StringUtils.count_vowels("hello"), 2)
        self.assertEqual(StringUtils.count_vowels("AEIOU"), 5)
        self.assertEqual(StringUtils.count_vowels(""), 0)
        self.assertEqual(StringUtils.count_vowels("bcdfg"), 0)
        self.assertEqual(StringUtils.count_vowels("Hello World"), 3)
    
    def test_capitalize_words(self):
        self.assertEqual(StringUtils.capitalize_words("hello world"), "Hello World")
        self.assertEqual(StringUtils.capitalize_words(""), "")
        self.assertEqual(StringUtils.capitalize_words("a"), "A")
        self.assertEqual(StringUtils.capitalize_words("hello   world"), "Hello   World")
    
    def test_remove_whitespace(self):
        self.assertEqual(StringUtils.remove_whitespace("hello world"), "helloworld")
        self.assertEqual(StringUtils.remove_whitespace(""), "")
        self.assertEqual(StringUtils.remove_whitespace("   "), "")
        self.assertEqual(StringUtils.remove_whitespace("a b c"), "abc")

if __name__ == '__main__':
    unittest.main()

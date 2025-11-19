class StringUtils:
    
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise TypeError(\"输入必须为字符串\")
        return s[::-1]
    
    @staticmethod
    def is_palindrome(s):
        if not isinstance(s, str):
            raise TypeError(\"输入必须为字符串\")
        s = s.lower().replace(\" \", \"\")
        return s == s[::-1]
    
    @staticmethod
    def count_vowels(s):
        if not isinstance(s, str):
            raise TypeError(\"输入必须为字符串\")
        vowels = \"aeiouAEIOU\"
        return sum(1 for char in s if char in vowels)
    
    @staticmethod
    def capitalize_words(s):
        if not isinstance(s, str):
            raise TypeError(\"输入必须为字符串\")
        return ' '.join(word.capitalize() for word in s.split())
    
    @staticmethod
    def remove_whitespace(s):
        if not isinstance(s, str):
            raise TypeError(\"输入必须为字符串\")
        return ''.join(s.split())

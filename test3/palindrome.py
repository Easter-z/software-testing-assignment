def is_palindrome(s):
    """
    判断字符串是否为回文
    忽略大小写和非字母数字字符
    """
    if not isinstance(s, str):
        raise TypeError("输入必须为字符串")
    
    # 清理字符串：转小写，移除非字母数字字符
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # 检查是否为空字符串
    if not cleaned:
        return False
    
    # 检查回文
    return cleaned == cleaned[::-1]


def is_palindrome_simple(s):
    """
    简单版本的回文判断
    不进行字符清理，直接比较
    """
    if not s:
        return False
    return s == s[::-1]

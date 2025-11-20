import pytest
from book_management import Book, User, BookManagementSystem, borrow_book

class TestBookManagement:
    def setup_method(self):
        """测试前置设置"""
        self.system = BookManagementSystem()
        
        # 添加测试用户
        self.user1 = User("U001", "张三")
        self.user2 = User("U002", "李四")
        self.system.add_user(self.user1)
        self.system.add_user(self.user2)
        
        # 添加测试图书
        self.book1 = Book("B001", "Python编程", "John Doe", 3)
        self.book2 = Book("B002", "软件测试", "Jane Smith", 1)
        self.book3 = Book("B003", "零库存图书", "Test Author", 0)
        self.system.add_book(self.book1)
        self.system.add_book(self.book2)
        self.system.add_book(self.book3)
    
    def test_borrow_book_success(self):
        """测试用例1: 正常借书流程"""
        result = borrow_book(self.system, "U001", "B001")
        assert "成功借阅《Python编程》" in result
        assert self.book1.stock == 2
    
    def test_borrow_book_user_not_exist(self):
        """测试用例2: 用户不存在"""
        with pytest.raises(ValueError, match="用户不存在"):
            borrow_book(self.system, "U999", "B001")
    
    def test_borrow_book_not_exist(self):
        """测试用例3: 图书不存在"""
        with pytest.raises(ValueError, match="图书不存在"):
            borrow_book(self.system, "U001", "B999")
    
    def test_borrow_book_zero_stock(self):
        """测试用例4: 库存为0的图书"""
        with pytest.raises(ValueError, match="图书库存不足"):
            borrow_book(self.system, "U001", "B003")
    
    def test_borrow_book_insufficient_stock_after_borrow(self):
        """测试用例5: 多次借阅导致库存不足"""
        borrow_book(self.system, "U001", "B002")
        with pytest.raises(ValueError, match="图书库存不足"):
            borrow_book(self.system, "U002", "B002")

class Book:
    def __init__(self, book_id, title, author, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0
    
    def decrease_stock(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            raise ValueError("图书库存不足")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class BookManagementSystem:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def add_user(self, user):
        self.users[user.user_id] = user
    
    def add_book(self, book):
        self.books[book.book_id] = book
    
    def borrow_book(self, user_id, book_id):
        # 1. 检查用户是否存在
        if user_id not in self.users:
            raise ValueError("用户不存在")
        
        # 2. 检查图书是否存在
        if book_id not in self.books:
            raise ValueError("图书不存在")
        
        user = self.users[user_id]
        book = self.books[book_id]
        
        # 3. 检查图书是否可借
        if not book.is_available():
            raise ValueError("图书库存不足，无法借阅")
        
        # 4. 执行借书操作
        book.decrease_stock()
        
        return f"用户 {user.name} 成功借阅《{book.title}》"

def borrow_book(system, user_id, book_id):
    return system.borrow_book(user_id, book_id)

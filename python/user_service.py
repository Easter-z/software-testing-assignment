class UserRepository:
    \"\"\"模拟数据库操作类\"\"\"
    
    def get_user_by_id(self, user_id):
        # 模拟数据库查询
        pass
    
    def save_user(self, user_data):
        # 模拟数据库保存
        pass
    
    def user_exists(self, username):
        # 检查用户名是否存在
        pass

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def get_user_profile(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise ValueError(\"用户不存在\")
        return {
            'id': user['id'],
            'username': user['username'],
            'email': user['email']
        }
    
    def register_user(self, username, email, password):
        if self.user_repository.user_exists(username):
            raise ValueError(\"用户名已存在\")
        
        user_data = {
            'username': username,
            'email': email,
            'password': password  # 实际中应该加密
        }
        
        return self.user_repository.save_user(user_data)
    
    def change_password(self, user_id, new_password):
        user = self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise ValueError(\"用户不存在\")
        
        user['password'] = new_password
        return self.user_repository.save_user(user)

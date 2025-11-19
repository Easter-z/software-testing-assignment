import unittest
from unittest.mock import Mock, patch
from user_service import UserService

class TestUserService(unittest.TestCase):
    
    def setUp(self):
        self.mock_repo = Mock()
        self.user_service = UserService(self.mock_repo)
    
    def test_get_user_profile_success(self):
        # 设置mock返回值
        mock_user = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'hashed_password'
        }
        self.mock_repo.get_user_by_id.return_value = mock_user
        
        # 执行测试
        result = self.user_service.get_user_profile(1)
        
        # 验证结果
        expected_result = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com'
        }
        self.assertEqual(result, expected_result)
        self.mock_repo.get_user_by_id.assert_called_once_with(1)
    
    def test_get_user_profile_user_not_found(self):
        # 设置mock返回None（用户不存在）
        self.mock_repo.get_user_by_id.return_value = None
        
        # 验证抛出异常
        with self.assertRaises(ValueError) as context:
            self.user_service.get_user_profile(999)
        
        self.assertEqual(str(context.exception), "用户不存在")
        self.mock_repo.get_user_by_id.assert_called_once_with(999)
    
    def test_register_user_success(self):
        # 设置mock返回值
        self.mock_repo.user_exists.return_value = False
        self.mock_repo.save_user.return_value = {
            'id': 1,
            'username': 'newuser',
            'email': 'new@example.com'
        }
        
        # 执行测试
        result = self.user_service.register_user(
            'newuser', 'new@example.com', 'password123'
        )
        
        # 验证结果
        self.assertEqual(result['username'], 'newuser')
        self.mock_repo.user_exists.assert_called_once_with('newuser')
        self.mock_repo.save_user.assert_called_once()
    
    def test_register_user_username_exists(self):
        # 设置mock返回值 - 用户名已存在
        self.mock_repo.user_exists.return_value = True
        
        # 验证抛出异常
        with self.assertRaises(ValueError) as context:
            self.user_service.register_user(
                'existinguser', 'test@example.com', 'password123'
            )
        
        self.assertEqual(str(context.exception), "用户名已存在")
        self.mock_repo.user_exists.assert_called_once_with('existinguser')
        self.mock_repo.save_user.assert_not_called()
    
    def test_change_password_success(self):
        # 设置mock返回值
        mock_user = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'old_password'
        }
        self.mock_repo.get_user_by_id.return_value = mock_user
        self.mock_repo.save_user.return_value = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'new_password'
        }
        
        # 执行测试
        result = self.user_service.change_password(1, 'new_password')
        
        # 验证结果
        self.assertEqual(result['password'], 'new_password')
        self.mock_repo.get_user_by_id.assert_called_once_with(1)
        self.mock_repo.save_user.assert_called_once()
    
    @patch('user_service.UserRepository')
    def test_user_service_initialization(self, MockUserRepository):
        # 测试依赖注入
        mock_repo_instance = MockUserRepository.return_value
        service = UserService(mock_repo_instance)
        
        self.assertEqual(service.user_repository, mock_repo_instance)

if __name__ == '__main__':
    unittest.main()

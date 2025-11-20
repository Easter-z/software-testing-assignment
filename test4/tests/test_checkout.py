import requests
import multiprocessing
import time
import pytest
from app.checkout_service import app

def run_server():
    """启动测试服务器"""
    app.run(port=5000, debug=False)

class TestCheckoutSystem:
    """Checkout 微服务系统测试"""
    
    @pytest.fixture(autouse=True)
    def setup_server(self):
        """在每个测试前启动服务器，测试后关闭"""
        self.server_process = multiprocessing.Process(target=run_server)
        self.server_process.start()
        time.sleep(2)  # 等待服务器启动
        yield
        self.server_process.terminate()
        self.server_process.join()
    
    def test_successful_checkout(self):
        """测试成功的结算流程"""
        data = {
            "items": [
                {"price": 20, "quantity": 3},
                {"price": 15, "quantity": 2}
            ]
        }
        response = requests.post("http://127.0.0.1:5000/checkout", json=data)
        
        assert response.status_code == 200
        result = response.json()
        assert result["total"] == 90
        assert result["shipping"] == 10
        assert result["final_total"] == 100
        assert result["status"] == "success"
    
    def test_empty_cart(self):
        """测试空购物车"""
        data = {"items": []}
        response = requests.post("http://127.0.0.1:5000/checkout", json=data)
        
        assert response.status_code == 400
        assert response.json()["error"] == "empty cart"
    
    def test_invalid_item_format(self):
        """测试无效的商品格式"""
        data = {
            "items": [
                {"price": 20}  # 缺少quantity字段
            ]
        }
        response = requests.post("http://127.0.0.1:5000/checkout", json=data)
        
        assert response.status_code == 400
        assert "invalid item format" in response.json()["error"]
    
    def test_health_check(self):
        """测试健康检查端点"""
        response = requests.get("http://127.0.0.1:5000/health")
        
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

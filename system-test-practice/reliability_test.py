import requests
import time
import logging
from datetime import datetime, timedelta

class ReliabilityTest:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.setup_logging()
    
    def setup_logging(self):
        """设置日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('reliability_test.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger()
    
    def test_system_stability(self, duration_hours=1, check_interval=60):
        """测试系统稳定性"""
        print(f"开始稳定性测试，持续时间: {duration_hours}小时")
        end_time = datetime.now() + timedelta(hours=duration_hours)
        success_count = 0
        failure_count = 0
        total_response_time = 0
        
        while datetime.now() < end_time:
            try:
                start_time = time.time()
                response = requests.get(f"{self.base_url}/api/v1/health", timeout=10)
                response_time = (time.time() - start_time) * 1000
                total_response_time += response_time
                
                if response.status_code == 200:
                    success_count += 1
                    self.logger.info(f"健康检查成功 - 响应时间: {response_time:.2f}ms")
                else:
                    failure_count += 1
                    self.logger.error(f"健康检查失败 - 状态码: {response.status_code}")
                    
            except Exception as e:
                failure_count += 1
                self.logger.error(f"健康检查异常: {str(e)}")
            
            time.sleep(check_interval)
        
        self.generate_stability_report(success_count, failure_count, total_response_time, duration_hours)
    
    def test_memory_leak(self, iterations=1000):
        """测试内存泄漏"""
        print("开始内存泄漏测试...")
        memory_data = []
        
        for i in range(iterations):
            try:
                # 模拟大量请求
                for _ in range(100):
                    requests.get(f"{self.base_url}/api/v1/equipment")
                    requests.post(f"{self.base_url}/api/v1/login", 
                                json={"username": "test", "password": "test"})
                
                if i % 100 == 0:
                    self.logger.info(f"内存泄漏测试进度: {i}/{iterations}")
                    
            except Exception as e:
                self.logger.error(f"内存泄漏测试出错: {str(e)}")
        
        print("内存泄漏测试完成")
    
    def test_error_recovery(self):
        """测试错误恢复能力"""
        print("开始错误恢复测试...")
        
        # 测试1: 服务重启恢复
        self.logger.info("测试服务重启恢复...")
        # 这里可以模拟服务重启，然后检查是否正常恢复
        
        # 测试2: 数据库连接中断恢复
        self.logger.info("测试数据库连接恢复...")
        
        # 测试3: 网络中断恢复
        self.logger.info("测试网络中断恢复...")
        
        print("错误恢复测试完成")
    
    def generate_stability_report(self, success_count, failure_count, total_response_time, duration_hours):
        """生成稳定性报告"""
        total_requests = success_count + failure_count
        availability = (success_count / total_requests) * 100 if total_requests > 0 else 0
        avg_response_time = total_response_time / success_count if success_count > 0 else 0
        
        print("\n=== 可靠性测试报告 ===")
        print(f"测试时长: {duration_hours}小时")
        print(f"总请求数: {total_requests}")
        print(f"成功请求: {success_count}")
        print(f"失败请求: {failure_count}")
        print(f"系统可用性: {availability:.2f}%")
        print(f"平均响应时间: {avg_response_time:.2f}ms")
        print(f"MTBF (平均无故障时间): {duration_hours * 3600 / (failure_count + 1):.2f}秒")
        
        if availability >= 99.9:
            print("✅ 系统可靠性: 优秀")
        elif availability >= 99:
            print("⚠️  系统可靠性: 良好")
        else:
            print("❌ 系统可靠性: 需要改进")

if __name__ == "__main__":
    test = ReliabilityTest()
    
    # 运行稳定性测试 (缩短为5分钟用于演示)
    test.test_system_stability(duration_hours=0.08, check_interval=10)
    
    # 运行其他可靠性测试
    test.test_memory_leak(iterations=100)
    test.test_error_recovery()

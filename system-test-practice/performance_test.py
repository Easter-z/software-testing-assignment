import time
import requests
import threading
import statistics
from concurrent.futures import ThreadPoolExecutor

class PerformanceTest:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.response_times = []
        self.error_count = 0
        
    def test_login_performance(self):
        """测试登录接口性能"""
        start_time = time.time()
        try:
            response = requests.post(
                f"{self.base_url}/api/v1/login",
                json={"username": "testuser", "password": "password123"},
                timeout=10
            )
            if response.status_code == 200:
                response_time = (time.time() - start_time) * 1000
                self.response_times.append(response_time)
            else:
                self.error_count += 1
        except Exception as e:
            self.error_count += 1
            print(f"请求失败: {e}")
    
    def test_equipment_list_performance(self):
        """测试设备列表查询性能"""
        start_time = time.time()
        try:
            response = requests.get(
                f"{self.base_url}/api/v1/equipment",
                timeout=10
            )
            if response.status_code == 200:
                response_time = (time.time() - start_time) * 1000
                self.response_times.append(response_time)
            else:
                self.error_count += 1
        except Exception as e:
            self.error_count += 1
    
    def run_concurrent_test(self, num_users=50, requests_per_user=10):
        """运行并发性能测试"""
        print(f"开始性能测试: {num_users}个用户，每个{requests_per_user}次请求")
        
        tasks = []
        for _ in range(num_users):
            for _ in range(requests_per_user):
                tasks.append(self.test_login_performance)
                tasks.append(self.test_equipment_list_performance)
        
        with ThreadPoolExecutor(max_workers=num_users) as executor:
            list(executor.map(lambda func: func(), tasks))
        
        # 输出性能报告
        self.generate_report(len(tasks))
    
    def generate_report(self, total_requests):
        """生成性能测试报告"""
        if not self.response_times:
            print("没有成功的请求数据")
            return
            
        print("\n=== 性能测试报告 ===")
        print(f"总请求数: {total_requests}")
        print(f"成功请求: {len(self.response_times)}")
        print(f"失败请求: {self.error_count}")
        print(f"成功率: {(len(self.response_times)/total_requests)*100:.2f}%")
        print(f"平均响应时间: {statistics.mean(self.response_times):.2f}ms")
        print(f"最小响应时间: {min(self.response_times):.2f}ms")
        print(f"最大响应时间: {max(self.response_times):.2f}ms")
        print(f"95%响应时间: {self.get_percentile(95):.2f}ms")
        print(f"标准差: {statistics.stdev(self.response_times) if len(self.response_times) > 1 else 0:.2f}ms")
    
    def get_percentile(self, percentile):
        """计算百分位数"""
        sorted_times = sorted(self.response_times)
        index = (percentile / 100) * (len(sorted_times) - 1)
        return sorted_times[int(index)]

if __name__ == "__main__":
    test = PerformanceTest()
    test.run_concurrent_test(num_users=20, requests_per_user=5)

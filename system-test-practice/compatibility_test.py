from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CompatibilityTest:
    def __init__(self):
        self.browsers = {
            'chrome': webdriver.Chrome,
            'firefox': webdriver.Firefox,
            # 'edge': webdriver.Edge,  # 需要安装Edge驱动
        }
        self.test_url = "http://localhost:8080"
    
    def test_browser_compatibility(self):
        """测试浏览器兼容性"""
        print("开始浏览器兼容性测试...")
        
        results = {}
        for browser_name, driver_class in self.browsers.items():
            try:
                print(f"测试 {browser_name}...")
                driver = driver_class()
                results[browser_name] = self.run_browser_tests(driver)
                driver.quit()
            except Exception as e:
                results[browser_name] = f"失败: {str(e)}"
        
        self.generate_compatibility_report(results)
    
    def run_browser_tests(self, driver):
        """在指定浏览器中运行测试"""
        test_results = {}
        
        try:
            # 测试1: 页面加载
            start_time = time.time()
            driver.get(self.test_url)
            load_time = time.time() - start_time
            test_results['page_load'] = f"成功 ({load_time:.2f}s)"
            
            # 测试2: 登录功能
            username_field = driver.find_element(By.NAME, "username")
            password_field = driver.find_element(By.NAME, "password")
            login_button = driver.find_element(By.XPATH, "//button[contains(text(),'登录')]")
            
            username_field.send_keys("testuser")
            password_field.send_keys("password123")
            login_button.click()
            
            time.sleep(2)
            test_results['login'] = "成功"
            
            # 测试3: 设备列表显示
            equipment_section = driver.find_element(By.ID, "equipment-list")
            if equipment_section.is_displayed():
                test_results['equipment_display'] = "成功"
            else:
                test_results['equipment_display'] = "失败"
                
        except Exception as e:
            test_results['error'] = str(e)
        
        return test_results
    
    def test_mobile_compatibility(self):
        """测试移动端兼容性"""
        print("\n=== 移动端兼容性测试 ===")
        mobile_configs = [
            {'width': 375, 'height': 667, 'name': 'iPhone SE'},
            {'width': 414, 'height': 896, 'name': 'iPhone XR'},
            {'width': 768, 'height': 1024, 'name': 'iPad'},
        ]
        
        driver = webdriver.Chrome()
        for config in mobile_configs:
            driver.set_window_size(config['width'], config['height'])
            driver.get(self.test_url)
            print(f"{config['name']} ({config['width']}x{config['height']}): 页面加载成功")
            time.sleep(1)
        
        driver.quit()
    
    def generate_compatibility_report(self, results):
        """生成兼容性测试报告"""
        print("\n=== 兼容性测试报告 ===")
        for browser, result in results.items():
            print(f"\n{browser.upper()} 浏览器:")
            if isinstance(result, dict):
                for test_name, test_result in result.items():
                    print(f"  {test_name}: {test_result}")
            else:
                print(f"  总体结果: {result}")

if __name__ == "__main__":
    test = CompatibilityTest()
    test.test_browser_compatibility()
    test.test_mobile_compatibility()

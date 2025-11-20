from zapv2 import ZAPv2
import time

class SecurityTest:
    def __init__(self, target_url="http://localhost:8080"):
        self.target_url = target_url
        self.zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
    
    def run_security_scan(self):
        """运行安全扫描"""
        print("开始安全扫描...")
        
        # 访问目标站点
        print("访问目标站点...")
        self.zap.urlopen(self.target_url)
        time.sleep(2)
        
        # 启动蜘蛛爬虫
        print("启动蜘蛛爬虫...")
        scan_id = self.zap.spider.scan(self.target_url)
        while int(self.zap.spider.status(scan_id)) < 100:
            print(f"蜘蛛爬虫进度: {self.zap.spider.status(scan_id)}%")
            time.sleep(2)
        
        # 启动主动扫描
        print("启动主动扫描...")
        ascan_id = self.zap.ascan.scan(self.target_url)
        while int(self.zap.ascan.status(ascan_id)) < 100:
            print(f"主动扫描进度: {self.zap.ascan.status(ascan_id)}%")
            time.sleep(5)
        
        # 生成安全报告
        self.generate_security_report()
    
    def generate_security_report(self):
        """生成安全报告"""
        print("\n=== 安全测试报告 ===")
        
        # 获取警报
        alerts = self.zap.core.alerts()
        
        # 按风险等级分类
        high_risk = [alert for alert in alerts if alert['risk'] == 'High']
        medium_risk = [alert for alert in alerts if alert['risk'] == 'Medium']
        low_risk = [alert for alert in alerts if alert['risk'] == 'Low']
        
        print(f"高风险漏洞: {len(high_risk)}个")
        for alert in high_risk:
            print(f"  - {alert['alert']} (URL: {alert['url']})")
        
        print(f"中风险漏洞: {len(medium_risk)}个")
        for alert in medium_risk:
            print(f"  - {alert['alert']}")
        
        print(f"低风险漏洞: {len(low_risk)}个")
        
        # 常见安全测试
        self.test_sql_injection()
        self.test_xss_vulnerability()
        self.test_authentication_issues()
    
    def test_sql_injection(self):
        """SQL注入测试"""
        print("\n=== SQL注入测试 ===")
        test_payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "1' UNION SELECT 1,2,3--"]
        
        for payload in test_payloads:
            try:
                response = requests.get(f"{self.target_url}/api/v1/users?username={payload}")
                if "error" in response.text.lower() or "sql" in response.text.lower():
                    print(f"⚠️  可能的SQL注入漏洞: {payload}")
            except:
                pass
    
    def test_xss_vulnerability(self):
        """XSS漏洞测试"""
        print("\n=== XSS漏洞测试 ===")
        xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>"]
        
        for payload in xss_payloads:
            try:
                response = requests.post(f"{self.target_url}/api/v1/comments", 
                                       json={"comment": payload})
                if payload in response.text:
                    print(f"⚠️  可能的XSS漏洞: {payload}")
            except:
                pass
    
    def test_authentication_issues(self):
        """认证问题测试"""
        print("\n=== 认证安全测试 ===")
        # 测试弱密码
        weak_passwords = ["123456", "password", "admin", "12345678"]
        for pwd in weak_passwords:
            response = requests.post(f"{self.target_url}/api/v1/login",
                                   json={"username": "admin", "password": pwd})
            if response.status_code == 200:
                print(f"⚠️  弱密码可能被接受: {pwd}")

if __name__ == "__main__":
    # 注意：需要先启动OWASP ZAP代理
    test = SecurityTest()
    test.run_security_scan()

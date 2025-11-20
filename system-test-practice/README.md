# 系统测试实践作业

## 测试工具掌握情况
- 性能测试工具: ☑ JMeter
- 安全测试工具: ☑ OWASP ZAP  
- 自动化测试工具: ☑ Selenium

## 测试内容覆盖

### 1. 负载测试
- 模拟100个并发用户
- 持续5分钟高负载场景
- 测试登录和设备查询接口

### 2. 性能测试  
- 响应时间分析
- 吞吐量测量
- 并发处理能力

### 3. 安全性测试
- SQL注入检测
- XSS漏洞扫描
- 认证安全测试
- OWASP Top 10漏洞检查

### 4. 兼容性测试
- 多浏览器测试(Chrome, Firefox)
- 移动端适配测试
- 响应式设计验证

### 5. 可靠性测试
- 系统稳定性验证
- 错误恢复能力测试
- 长时间运行可靠性

## 运行说明

### 环境要求
- Python 3.8+
- Java 8+ (JMeter)
- OWASP ZAP
- 浏览器驱动

### 运行测试
```bash
# 安装依赖
pip install -r requirements.txt

# 运行性能测试
python performance_test.py

# 运行安全测试 (需要先启动ZAP)
python security_test.py

# 运行兼容性测试
python compatibility_test.py

# 运行可靠性测试
python reliability_test.py

# 软件测试课程作业

## 项目说明

本项目包含软件测试课程的四个作业练习，涵盖单元测试的核心概念和实践。

## 作业内容

1. **作业1**: Calculator类单元测试（Java/JUnit）
2. **作业2**: 字符串处理函数测试（Python/unittest）
3. **作业3**: 边界值分析与等价类划分应用
4. **作业4**: Mock对象在单元测试中的应用

## 项目结构

\\  
software-testing-assignment/
├── java/                 # Java相关代码
│   ├── Calculator.java
│   ├── CalculatorTest.java
│   └── pom.xml
├── python/               # Python相关代码
│   ├── string\_utils.py
│   ├── test\_string\_utils.py
│   ├── age\_validator.py
│   ├── test\_age\_validator.py
│   ├── user\_service.py
│   └── test\_user\_service.py
├── docs/                 # 文档资料
├── reports/              # 测试报告
├── .gitignore           # Git忽略配置
└── README.md           # 项目说明
\\\\

## 运行说明

### Java测试

\\\\
cd java
mvn test
mvn jacoco:report
\\\\

### Python测试

\\\\
cd python
pip install coverage
coverage run -m unittest discover
coverage html
\\\\

## 测试覆盖率

* Java覆盖率报告: \\java/target/site/jacoco/index.html\\
* Python覆盖率报告: \\python/htmlcov/index.html\\

## 作者

* 姓名: \[张茂成]
* 学号: \[1202422055]
* 课程: 软件测试

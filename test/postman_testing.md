\# Postman API 测试作业



\## 工具安装

1\. 访问 https://www.postman.com/downloads/

2\. 下载并安装Postman桌面版

3\. 注册免费账户



\## 最简单的API测试示例



\### 测试目标API

使用免费的测试API：https://jsonplaceholder.typicode.com



\### 测试步骤



\#### 1. 创建新的Collection

\- 点击 "Collections" → "New Collection"

\- 名称: "Software Testing Assignment"



\#### 2. 添加GET请求测试

\- 在Collection中点击 "Add Request"

\- 请求名称: "Get All Posts"

\- 方法: GET

\- URL: https://jsonplaceholder.typicode.com/posts



\#### 3. 添加测试脚本

在 "Tests" 标签页中添加：



```javascript

// 验证状态码

pm.test("Status code is 200", function () {

&nbsp;   pm.response.to.have.status(200);

});



// 验证响应时间

pm.test("Response time is less than 1000ms", function () {

&nbsp;   pm.expect(pm.response.responseTime).to.be.below(1000);

});



// 验证响应包含数据

pm.test("Response has posts data", function () {

&nbsp;   const response = pm.response.json();

&nbsp;   pm.expect(response).to.be.an('array');

&nbsp;   pm.expect(response.length).to.be.above(0);

});



// 验证数据结构

pm.test("Post has required fields", function () {

&nbsp;   const response = pm.response.json();

&nbsp;   pm.expect(response\[0]).to.have.property('id');

&nbsp;   pm.expect(response\[0]).to.have.property('title');

&nbsp;   pm.expect(response\[0]).to.have.property('body');

&nbsp;   pm.expect(response\[0]).to.have.property('userId');

});


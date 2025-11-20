\# 软件测试作业 - 缺陷检测与分析



\## 作业要求

分析包含3个缺陷的Python程序片段，设计测试用例并提交测试报告。



\## 识别出的缺陷

1\. \*\*divide函数\*\*: 未检查除数为0

2\. \*\*find\_max函数\*\*: 初始值设为0，全负数列表返回错误结果  

3\. \*\*get\_item函数\*\*: 未检查索引越界



\## 测试用例设计

设计了8个测试用例，覆盖正常情况和异常情况：



| 用例ID | 测试函数 | 输入数据 | 预期结果 | 测试目的 |

|--------|----------|----------|----------|----------|

| TC-001 | divide | a=10, b=2 | 5.0 | 正常除法运算 |

| TC-002 | divide | a=10, b=0 | 抛出ZeroDivisionError | 除数为零处理 |

| TC-003 | divide | a=0, b=5 | 0.0 | 被除数为零 |

| TC-004 | find\_max | lst=\[1,5,3,9,2] | 9 | 正常找最大值 |

| TC-005 | find\_max | lst=\[-1,-5,-3,-9] | -1 | 全负数列表最大值 |

| TC-006 | find\_max | lst=\[] | 0 | 空列表处理 |

| TC-007 | get\_item | lst=\[10,20,30], idx=1 | 20 | 正常索引访问 |

| TC-008 | get\_item | lst=\[10,20,30], idx=5 | 抛出IndexError | 索引越界处理 |



\## 文件说明

\- `defective\_functions.py`: 包含3个缺陷的原始代码

\- `test\_defective\_functions.py`: 测试代码和报告生成

\- `fixed\_functions.py`: 修复后的代码

\- `requirements.txt`: Python依赖



\## 运行测试

```bash

cd test

python test\_defective\_functions.py


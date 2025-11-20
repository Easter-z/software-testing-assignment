#!/usr/bin/env python3

import subprocess
import sys
import re
import os

class CodeReviewChecklist:
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def check_test_coverage(self):
        """检查测试覆盖率"""
        try:
            result = subprocess.run(
                ['mvn', 'jacoco:check'],
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode != 0:
                self.errors.append("❌ 测试覆盖率未达到80%要求")
                print("测试覆盖率检查失败详情:")
                print(result.stdout)
                print(result.stderr)
            else:
                print("✅ 测试覆盖率检查通过")
        except subprocess.TimeoutExpired:
            self.errors.append("❌ 测试覆盖率检查超时")
        except Exception as e:
            self.warnings.append(f"⚠️  无法检查测试覆盖率: {e}")
    
    def check_static_analysis(self):
        """检查静态分析结果"""
        try:
            result = subprocess.run(
                ['mvn', 'spotbugs:check'],
                capture_output=True,
                text=True,
                timeout=120
            )
            if "BUGS" in result.stdout or result.returncode != 0:
                self.errors.append("❌ 静态分析发现代码缺陷")
                print("静态分析失败详情:")
                print(result.stdout)
            else:
                print("✅ 静态分析通过")
        except subprocess.TimeoutExpired:
            self.errors.append("❌ 静态分析检查超时")
        except Exception as e:
            self.warnings.append(f"⚠️  无法进行静态分析: {e}")
    
    def check_exception_handling(self, file_path):
        """检查异常处理"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查是否捕获了特定异常
            if "FileNotFoundException" in content and "catch" not in content:
                self.warnings.append(f"⚠️  {file_path}: 可能缺少FileNotFoundException处理")
                
            # 检查是否处理了空指针
            if "NullPointerException" in content and "catch" not in content:
                self.errors.append(f"❌ {file_path}: 存在空指针异常风险")
                
            # 检查是否有输入验证
            if "public" in content and "void" in content and "validate" not in content:
                if "String" in content or "int" in content:
                    self.warnings.append(f"⚠️  {file_path}: 建议添加输入验证")
                    
        except Exception as e:
            self.warnings.append(f"⚠️  无法检查文件 {file_path}: {e}")
    
    def run_java_tests(self):
        """运行Java单元测试"""
        try:
            result = subprocess.run(
                ['mvn', 'test'],
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode != 0:
                self.errors.append("❌ 单元测试执行失败")
                print("单元测试失败详情:")
                print(result.stdout)
                print(result.stderr)
            else:
                print("✅ 所有单元测试通过")
        except subprocess.TimeoutExpired:
            self.errors.append("❌ 单元测试执行超时")
        except Exception as e:
            self.errors.append(f"❌ 无法执行单元测试: {e}")
    
    def run_checks(self):
        """运行所有检查"""
        print("开始代码质量检查...")
        print("=" * 50)
        
        self.check_test_coverage()
        self.check_static_analysis()
        self.run_java_tests()
        
        # 检查Java文件
        print("\n检查Java文件异常处理...")
        if os.path.exists('.'):
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.java'):
                        full_path = os.path.join(root, file)
                        self.check_exception_handling(full_path)
        
        # 输出结果
        print("\n" + "=" * 50)
        print("代码质量检查完成")
        
        if self.errors:
            print("\n❌ 代码审查失败:")
            for error in self.errors:
                print(f"  - {error}")
            return False
        else:
            print("\n✅ 代码审查通过")
            if self.warnings:
                print("\n⚠️  警告信息:")
                for warning in self.warnings:
                    print(f"  - {warning}")
            return True

if __name__ == "__main__":
    checklist = CodeReviewChecklist()
    success = checklist.run_checks()
    sys.exit(0 if success else 1)

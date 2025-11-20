package com.lab.equipment.test;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import com.lab.equipment.utils.ValidationUtils;
import com.lab.equipment.utils.ValidationException;

/**
 * 安全测试 - 预防安全相关缺陷
 */
public class SecurityTest {
    
    @Test
    public void testSqlInjectionPrevention() {
        String[] sqlInjectionAttempts = {
            "admin' OR '1'='1",
            "'; DROP TABLE users; --",
            "1' UNION SELECT username, password FROM users --",
            "OR 1=1",
            "AND 1=1"
        };
        
        for (String maliciousInput : sqlInjectionAttempts) {
            assertThrows(SecurityException.class, 
                () -> ValidationUtils.validateInput(maliciousInput, "用户名", 100));
        }
    }
    
    @Test
    public void testXssPreventionInInput() {
        String[] xssAttempts = {
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert(1)>",
            "javascript:alert('xss')",
            "onload=alert('xss')"
        };
        
        // 验证这些输入不会被直接拒绝（业务逻辑处理）
        for (String xssInput : xssAttempts) {
            assertDoesNotThrow(() -> 
                ValidationUtils.validateInput(xssInput, "评论内容", 500));
        }
    }
}

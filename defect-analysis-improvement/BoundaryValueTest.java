package com.lab.equipment.test;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import com.lab.equipment.utils.ValidationUtils;
import com.lab.equipment.utils.ValidationException;
import java.time.LocalDateTime;

/**
 * 边界值测试 - 针对常见缺陷场景
 */
public class BoundaryValueTest {
    
    @Test
    public void testInputValidationBoundaryValues() {
        // 测试空值和空字符串
        assertThrows(ValidationException.class, 
            () -> ValidationUtils.validateInput(null, "用户名", 50));
        assertThrows(ValidationException.class, 
            () -> ValidationUtils.validateInput("", "用户名", 50));
        assertThrows(ValidationException.class, 
            () -> ValidationUtils.validateInput("   ", "用户名", 50));
        
        // 测试长度边界
        String maxLengthString = "a".repeat(50);
        String overLengthString = "a".repeat(51);
        
        assertDoesNotThrow(() -> ValidationUtils.validateInput(maxLengthString, "用户名", 50));
        assertThrows(ValidationException.class, 
            () -> ValidationUtils.validateInput(overLengthString, "用户名", 50));
    }
    
    @Test
    public void testNumberRangeBoundaryValues() {
        // 测试数字边界值
        int[] invalidNumbers = {0, -1, 101}; // 设备数量：1-100
        int[] validNumbers = {1, 50, 100};
        
        for (int num : invalidNumbers) {
            assertThrows(ValidationException.class, 
                () -> ValidationUtils.validateNumberRange(num, 1, 100, "设备数量"));
        }
        
        for (int num : validNumbers) {
            assertDoesNotThrow(() -> 
                ValidationUtils.validateNumberRange(num, 1, 100, "设备数量"));
        }
    }
    
    @Test
    public void testDateTimeBoundaryValues() {
        // 测试时间边界值
        LocalDateTime pastTime = LocalDateTime.now().minusMinutes(1);
        LocalDateTime futureTime = LocalDateTime.now().plusMinutes(1);
        
        assertThrows(ValidationException.class, 
            () -> ValidationUtils.validateFutureDate(pastTime, "预约时间"));
        assertDoesNotThrow(() -> 
            ValidationUtils.validateFutureDate(futureTime, "预约时间"));
    }
    
    @Test
    public void testEmailValidationBoundaryValues() {
        String[] invalidEmails = {
            null,
            "",
            "invalid",
            "invalid@",
            "@domain.com",
            "invalid@domain"
        };
        
        String[] validEmails = {
            "test@example.com",
            "user.name@domain.co.uk",
            "user+tag@example.org"
        };
        
        for (String email : invalidEmails) {
            assertThrows(ValidationException.class, 
                () -> ValidationUtils.validateEmail(email));
        }
        
        for (String email : validEmails) {
            assertDoesNotThrow(() -> ValidationUtils.validateEmail(email));
        }
    }
}

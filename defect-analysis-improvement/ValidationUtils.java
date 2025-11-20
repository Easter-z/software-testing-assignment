package com.lab.equipment.utils;

/**
 * 输入验证工具类 - 预防边界条件缺陷
 */
public class ValidationUtils {
    
    /**
     * 通用输入验证方法
     */
    public static void validateInput(String input, String fieldName, int maxLength) {
        if (input == null) {
            throw new ValidationException(fieldName + "不能为空");
        }
        if (input.trim().isEmpty()) {
            throw new ValidationException(fieldName + "不能为空字符串");
        }
        if (input.length() > maxLength) {
            throw new ValidationException(fieldName + "长度不能超过" + maxLength + "个字符");
        }
        // SQL注入检测
        if (containsSqlInjection(input)) {
            throw new SecurityException("检测到非法输入内容");
        }
    }
    
    /**
     * 邮箱格式验证
     */
    public static void validateEmail(String email) {
        if (email == null || !email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new ValidationException("邮箱格式不正确");
        }
    }
    
    /**
     * 数字范围验证
     */
    public static void validateNumberRange(int number, int min, int max, String fieldName) {
        if (number < min || number > max) {
            throw new ValidationException(fieldName + "必须在" + min + "到" + max + "之间");
        }
    }
    
    /**
     * 日期验证 - 防止时间相关缺陷
     */
    public static void validateFutureDate(java.time.LocalDateTime date, String fieldName) {
        if (date.isBefore(java.time.LocalDateTime.now())) {
            throw new ValidationException(fieldName + "必须是未来时间");
        }
    }
    
    private static boolean containsSqlInjection(String input) {
        String[] sqlKeywords = {"select", "insert", "delete", "update", "drop", "union", "or", "and"};
        String lowerInput = input.toLowerCase();
        for (String keyword : sqlKeywords) {
            if (lowerInput.contains(keyword + " ") || lowerInput.contains(keyword + ";")) {
                return true;
            }
        }
        return false;
    }
}

/**
 * 自定义验证异常
 */
class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}

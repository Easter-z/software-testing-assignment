package com.lab.equipment.handler;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ControllerAdvice;
import com.lab.equipment.utils.ValidationException;

/**
 * 全局异常处理器 - 统一异常处理，预防缺陷
 */
@ControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    /**
     * 处理验证异常
     */
    @ExceptionHandler(ValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(ValidationException ex) {
        logger.warn("输入验证失败: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", ex.getMessage());
        return ResponseEntity.badRequest().body(error);
    }
    
    /**
     * 处理安全异常
     */
    @ExceptionHandler(SecurityException.class)
    public ResponseEntity<ErrorResponse> handleSecurityException(SecurityException ex) {
        logger.error("安全异常: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse("SECURITY_ERROR", "请求包含安全风险");
        return ResponseEntity.status(403).body(error);
    }
    
    /**
     * 处理空指针异常
     */
    @ExceptionHandler(NullPointerException.class)
    public ResponseEntity<ErrorResponse> handleNullPointerException(NullPointerException ex) {
        logger.error("空指针异常: ", ex);
        ErrorResponse error = new ErrorResponse("NULL_POINTER_ERROR", "系统内部错误");
        return ResponseEntity.status(500).body(error);
    }
    
    /**
     * 处理所有未捕获异常
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        logger.error("系统异常: ", ex);
        ErrorResponse error = new ErrorResponse("SYSTEM_ERROR", "系统繁忙，请稍后重试");
        return ResponseEntity.status(500).body(error);
    }
}

/**
 * 错误响应实体
 */
class ErrorResponse {
    private String code;
    private String message;
    private long timestamp;
    
    public ErrorResponse(String code, String message) {
        this.code = code;
        this.message = message;
        this.timestamp = System.currentTimeMillis();
    }
    
    // getters and setters
    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }
    
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    
    public long getTimestamp() { return timestamp; }
    public void setTimestamp(long timestamp) { this.timestamp = timestamp; }
}

public class Calculator {
    
    public int add(int a, int b) {
        return a + b;
    }
    
    public int subtract(int a, int b) {
        return a - b;
    }
    
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public double divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException(\"除数不能为零\");
        }
        return (double) a / b;
    }
    
    public int power(int base, int exponent) {
        if (exponent < 0) {
            throw new IllegalArgumentException(\"指数不能为负数\");
        }
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        return result;
    }
}

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calculator = new Calculator();

    @Test void testAdd() { assertEquals(5, calculator.add(2, 3)); }
    @Test void testSubtract() { assertEquals(1, calculator.subtract(3, 2)); }
    @Test void testMultiply() { assertEquals(6, calculator.multiply(2, 3)); }
    @Test void testDivide() { assertEquals(2.0, calculator.divide(6, 3)); }
    @Test void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> calculator.divide(5, 0));
    }
    @Test void testPower() { assertEquals(8, calculator.power(2, 3)); }
    @Test void testPowerWithNegativeExponent() {
        assertThrows(IllegalArgumentException.class, () -> calculator.power(2, -1));
    }
}

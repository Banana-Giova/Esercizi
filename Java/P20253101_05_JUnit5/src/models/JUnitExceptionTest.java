package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class JUnitExceptionTest {
	@Test
	void testTestException() {
		System.out.println("JUnit Exception Test in esecuzione!");
		JUnitException ex = new JUnitException();
		Exception exception = assertThrows(Exception.class, () -> ex.testException());
		assertEquals("Eccezione JUnit", exception.getMessage());
	}
}

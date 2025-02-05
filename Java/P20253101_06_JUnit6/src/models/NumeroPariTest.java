package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class NumeroPariTest {
	
	@ParameterizedTest
	@CsvSource({
		"1, false",
		"2, true",
		"3, false",
		"4, true",
		"5, false"
	})
	public void testNumeroPari(int num, boolean result) {
		System.out.println("Test Numero Pari numero " + num + " in esecuzione!");
		assertEquals(result, NumeroPari.numeroPari(num));
	}
}

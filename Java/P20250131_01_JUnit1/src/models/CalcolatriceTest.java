package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CalcolatriceTest {
	
	@Test
	public static void testSomma() {
		System.out.println("Test somma eseguito!");
		assertEquals(5, Calcolatrice.somma(3, 2));
	}
}

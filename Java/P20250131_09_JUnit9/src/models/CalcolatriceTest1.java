package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CalcolatriceTest1 {
	
	@Test
	public void testSomma() {
		System.out.println("Test somma chiamato!");
		assertEquals(7, Calcolatrice1.somma(5, 2));
	}
	@Test
	public void testSottrazione() {
		System.out.println("Test sottrazione chiamato!");
		assertEquals(3, Calcolatrice1.sottrazione(5, 2));
	}	
}

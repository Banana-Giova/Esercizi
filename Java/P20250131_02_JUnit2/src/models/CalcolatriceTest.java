package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CalcolatriceTest {
	
	@Test
	public void testSomma() {
		System.out.println("Test somma chiamato!");
		assertEquals(7, Calcolatrice.somma(5, 2));
	}
	@Test
	public void testSottrazione() {
		System.out.println("Test sottrazione chiamato!");
		assertEquals(3, Calcolatrice.sottrazione(5, 2));
	}
	@Test
	public void testMoltiplicazione() {
		System.out.println("Test moltiplicazione chiamato!");
		assertEquals(10, Calcolatrice.moltiplicazione(5, 2));
	}
	@Test
	public void testDivisione() {
		System.out.println("Test divisione chiamato!");
		assertEquals(2.5, Calcolatrice.divisione(5, 2));
	}
	
	
}

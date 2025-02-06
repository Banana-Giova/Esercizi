package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class CalcolatriceTest2 {
	@Test
	public void testMoltiplicazione() {
		System.out.println("Test moltiplicazione chiamato!");
		assertEquals(10, Calcolatrice2.moltiplicazione(5, 2));
	}
	@Test
	public void testDivisione() {
		System.out.println("Test divisione chiamato!");
		assertEquals(2.5, Calcolatrice2.divisione(5, 2));
	}
	
}

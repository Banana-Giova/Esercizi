package models;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalendarioTest {
	
	@Test
	public void calendarioTest1() {
		System.out.println("Test Calendario 1 in esecuzione!");
		String giorno_settimana = Calendario.CalendarCheck(31, 01, 2025);
		assertEquals("Venerdì", giorno_settimana);
	}
	
	@Test
	public void calendarioTest2() {
		System.out.println("Test Calendario 2 in esecuzione!");
		String giorno_settimana = Calendario.CalendarCheck(31, 02, 2025);
		assertEquals("ERROR", giorno_settimana);
	}
	
	@Test
	public void calendarioTest3() {
		System.out.println("Test Calendario 3 in esecuzione!");
		String giorno_settimana = Calendario.CalendarCheck(31, 01, 2024);
		assertEquals("Mercoledì", giorno_settimana);
	}
	
	@Test
	public void calendarioTest4() {
		System.out.println("Test Calendario 4 in esecuzione!");
		String giorno_settimana = Calendario.CalendarCheck(41, 333, 3333);
		assertEquals("ERROR", giorno_settimana);
	}
}

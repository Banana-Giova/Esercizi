package models;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class ArchivioTest {
	private ArchivioStudenti archivio;
	@BeforeEach
	public void setup() {
		archivio = new ArchivioStudenti();
		archivio.addStudente("Rino", "Paidolo", 32, "NA79W8DHY");
		archivio.addStudente("Samuele", "Cammello", 23, "NA789788DHY");
		archivio.addStudente("Peppe", "Brescia", 42, "jc89H389");
		archivio.addStudente("Alessandro", "Sereni", 673, "NAHMANGADDYUM");
	}
	
	
	@Test
	public void testArchivio1( ) {
		System.out.println("Test Archivio 1 in esecuzione!");
		assertEquals(4, archivio.numStudenti());
	}
	
	@Test
	public void testArchivio2( ) {
		System.out.println("Test Archivio 2 in esecuzione!");
		archivio.addStudente("Rino", "Paidolo", 32, "NA79W8DHY");
		assertEquals(4, archivio.numStudenti());
	}
	
	@Test
	public void testArchivio3( ) {
		System.out.println("Test Archivio 3 in esecuzione!");
		archivio.addStudente("Sandro", "Maialozzo", 2, "CHA98CH");
		assertEquals(5, archivio.numStudenti());
	}
	
	@Test
	public void testArchivio4( ) {
		System.out.println("Test Archivio 4 in esecuzione!");
		archivio.addStudente("Sandro", "Maialozzo", 2, "CHA98CH");
		archivio.addStudente("Susino", "Maialino", 3, "CHA98CH");
		assertEquals(5, archivio.numStudenti());
	}
	
	@Test
	public void testArchivio5( ) {
		System.out.println("Test Archivio 5 in esecuzione!");
		archivio.clearStudenti();
		assertEquals(0, archivio.numStudenti());
	}
	
	@Test
	public void testArchivio6( ) {
		System.out.println("Test Archivio 6 in esecuzione!");
		archivio.clearStudenti();
		archivio.addStudente("Susino", "Maialino", 3, "CHA98CH");
		assertEquals(1, archivio.numStudenti());
	}
	@Test
	public void testArchivio7( ) {
		System.out.println("Test Archivio 7 in esecuzione!");
		archivio.removeStudente("NA79W8DHY");
		assertEquals(3, archivio.numStudenti());
	}
	@Test
	public void testArchivio8( ) {
		System.out.println("Test Archivio 8 in esecuzione!");
		archivio.removeStudente("f");
		assertEquals(4, archivio.numStudenti());
	}
}

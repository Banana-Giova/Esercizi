package models;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class TestStringhe {
	
	@Test
	public void testCharCount1() {
		System.out.println("Test Char Count 1 eseguito!");
		assertEquals(2, EsempiStringhe.charCount('o', "oblio"));
	}
	
	@Test
	public void testCharCount2() {
		System.out.println("Test Char Count 2 eseguito!");
		assertNotEquals(3, EsempiStringhe.charCount('o', "oblio"));
	}
	
	@Test
	public void testPalindrome1() {
		System.out.println("Test Palindrome 1 eseguito!");
		assertEquals(false, EsempiStringhe.palindrome("oblio"));
	}
	
	@Test
	public void testPalindrome2() {
		System.out.println("Test Palindrome 2 eseguito!");
		assertEquals(true, EsempiStringhe.palindrome("onano"));
	}
}

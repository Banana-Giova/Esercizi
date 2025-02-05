package models;

public class EsempiStringhe {
	public static int charCount(char alnum, String word) {
		int count = 0;
		for (char ch : word.toCharArray()) {
			if (ch == alnum) {
				count++;
			}
		}
		return count;
	}
	public static boolean palindrome(String word) {
		return (word.equals(new StringBuilder(word).reverse().toString()) ? (true) : (false));
	}
}

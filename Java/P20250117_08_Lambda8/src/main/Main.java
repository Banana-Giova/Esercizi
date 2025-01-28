package main;
public class Main {

	public static void main(String[] args) {
		VerificatoreParola concas = (string) -> (new StringBuilder(string).reverse().toString()).equals(string);
		System.out.println(concas.verifica("elatelaletale"));
		System.out.println(concas.verifica("Cavallo"));
	}

}

package main;
public class Main {

	public static void main(String[] args) {
		VerificatoreParola concas = (string) -> (string.trim())=="";
		System.out.println(concas.verifica("       "));
		System.out.println(concas.verifica("Cavallo"));
		System.out.println(concas.verifica(""));
	}

}

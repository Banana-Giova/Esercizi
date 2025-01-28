package main;
public class Main {

	public static void main(String[] args) {
		VerificatoreNumero vernu = (int1) -> int1 >= 0;
		System.out.println(vernu.verifica(47));
		System.out.println(vernu.verifica(-47));
	}

}

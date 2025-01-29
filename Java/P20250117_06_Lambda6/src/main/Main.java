package main;

public class Main {

	public static void main(String[] args) {
		VerificatorePari verpar = (int1) -> (int1 % 2) == 0;
		System.out.println(verpar.verifica(47));
		System.out.println(verpar.verifica(48));
	}

}

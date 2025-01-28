package main;
public class Main {

	public static void main(String[] args) {
		VerificatoreParola verpa = (string1,int1) -> string1.length() == int1;
		System.out.println(verpa.verifica("Cavallo", 7));
		System.out.println(verpa.verifica("Cavallo", 8));
	}

}

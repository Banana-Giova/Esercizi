package main;
public class Main {

	public static void main(String[] args) {
		CalcolatorePotenza calpo = (base,esponente) -> {
			int output = base;
			for (int i = 1; i < esponente; i++) {
				output *= base;
			}
			return output;
		};
		System.out.println(calpo.calcola(47, 4));
	}

}

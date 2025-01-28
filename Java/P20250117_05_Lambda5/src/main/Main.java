package main;
public class Main {

	public static void main(String[] args) {
		ConcatenaStringhe concas = (string1,string2) -> string1 + string2;
		System.out.println(concas.concatena("Cavallo", " Volante"));
		System.out.println(concas.concatena("Cavallo", " Gigante"));
	}

}

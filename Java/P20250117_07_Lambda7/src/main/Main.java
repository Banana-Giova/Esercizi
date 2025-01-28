package main;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Sommatore concas = (lista) -> {
			int output = 0;
			for (int i = 0; i < lista.size(); i++) {
				lista.get(i);
				output += lista.get(i);
			}
			return output;
		};
        ArrayList<Integer> myLista = new ArrayList<Integer>() {
            {
                add(3);
                add(5);
                add(7);
            }
        };
        System.out.println(concas.sommatore(myLista));
	}

}

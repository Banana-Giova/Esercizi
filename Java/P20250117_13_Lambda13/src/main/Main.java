package main;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		OrdinaLista ordist = (lista) -> {
			int list_len = lista.size();
			boolean swapped;
			
			for (int i = 0; i < (list_len-1); i++) {
				swapped = false;
				for (int j = 0; j < list_len - 1 - i; j++) {
				    if (lista.get(j).compareTo(lista.get(j+1)) > 0) {
				        String temp = lista.get(j);
				        lista.set(j, lista.get(j+1));
				        lista.set(j+1, temp);
				        swapped = true;
				    }
				}
				if (!swapped) break;
			}
			return lista;
		};

		List<String> colors = Arrays.asList("red", "green", "blue", "black", "pink");
        System.out.println("Prima dell'ordinamento:");
		printList(colors);
        ordist.ordina(colors);
        System.out.println("\n\nDopo l'ordinamento:");
        printList(colors);
	}
	
	public static void printList(List<String> list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " ");
        };	
	}
}
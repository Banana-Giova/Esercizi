package models;
import java.util.*;

public class ListaNumeri {
    private static List<Integer> numeri;

    private ListaNumeri() {
        numeri = new ArrayList<>();
        // Aggiungi numeri alla lista
        addNumeri();
    }

    private void addNumeri() {
        numeri.add(1000);
        numeri.add(2000);
        numeri.add(3000);
        numeri.add(4000);
        numeri.add(5000);
        numeri.add(6000);
        numeri.add(7000);
        numeri.add(8000);
        numeri.add(9000);
        numeri.add(10000);
    }
    
    protected static int getRandInt() {
        Random random = new Random();
        int indiceCasuale = random.nextInt(numeri.size());
        return numeri.get(indiceCasuale); 
    }
}
package models;
import java.util.*;

public class ListaNumeri {
    private List<Integer> numeri;
    private static int count_clienti = 0;

    private ListaNumeri() {
        numeri = new ArrayList<>();
        addNumeri();
    }
    
    protected synchronized static int getCountClienti() {
    	count_clienti++;
    	return count_clienti;
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
        numeri.add(1000);
    }
    
    protected static int getRandInt() {
        Random random = new Random();
        ListaNumeri linu = new ListaNumeri();
        int indiceCasuale = random.nextInt(linu.numeri.size());
        return linu.numeri.get(indiceCasuale); 
    }
}
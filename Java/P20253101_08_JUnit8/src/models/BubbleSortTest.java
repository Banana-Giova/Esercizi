package models;
import static org.junit.Assert.*;
import java.util.*;
import org.junit.jupiter.api.RepeatedTest;

public class BubbleSortTest {
	
	@RepeatedTest(5)
	public void testBubbleSort() {
        List<Integer> listaCasuale = new ArrayList<>();
        Random rand = new Random();
        
        for (int i = 0; i < 10; i++) {
            listaCasuale.add(rand.nextInt(100) + 1);
        }
        
        System.out.println("Eseguo un Bubble Sort Test!");
        
        boolean error = false;
        int temp = -1;
        List<Integer> listaOrdinata = BubbleSort.bubbleSort(listaCasuale);
        
        for (int num : listaOrdinata) {
        	if (temp == -1) {
        		temp = num;
        		continue;
        	}
        	if (temp > num) {
        		error = true;
        	}
        }
        assertFalse(error);
	}
}

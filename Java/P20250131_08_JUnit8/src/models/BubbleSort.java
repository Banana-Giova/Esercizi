package models;
import java.util.List;

public class BubbleSort {
    public static List<Integer> bubbleSort(List<Integer> lista) {
        int list_len = lista.size();
        boolean swapped;
    
        for (int i = 0; i < (list_len - 1); i++) {
            swapped = false;
            for (int j = 0; j < list_len - 1 - i; j++) {
                if (lista.get(j) > lista.get(j + 1)) {
                    int temp = lista.get(j);
                    lista.set(j, lista.get(j + 1));
                    lista.set(j + 1, temp);
                    swapped = true;
                }
            }
            if (!swapped)
                break;
        }
        return lista;
    }
}

package models;
import java.util.List;


public interface Ordinabile {
	List<Prodotto> sortByPrice(List<Prodotto> products);
}

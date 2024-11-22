package models;
import java.util.*;

public class ProductManager implements Ordinabile {
	private ArrayList<Prodotto> prod_list = new ArrayList<Prodotto>();
	
	public void addProd(Prodotto new_prod) {
		prod_list.add(new_prod);
	}
	
	public void viewProd() {
		for (Prodotto product : prod_list) {
			System.out.println(product.toString());	
		}
	}
	
	public ArrayList<Prodotto> getProdList() {
		return prod_list;
	}
	
	@Override
	public List<Prodotto> sortByPrice(List<Prodotto> products) {
		Collections.sort(prod_list);
		return prod_list;
	}	
}
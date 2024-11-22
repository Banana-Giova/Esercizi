package models;

public class Abbigliamento extends Prodotto {
	
	public Abbigliamento(String name, Double price, String categoria) {
		super(name, price, categoria);
	}
	
	@Override
	public Double calculateDiscount() {
		if (categoria == "Articolo Invernale") {
			return price*0.15;
		} else {
			return 0.0;
		}
	}
}
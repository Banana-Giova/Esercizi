package models;

public class Elettronica extends Prodotto {
	
	public Elettronica(String name, Double price, String categoria) {
		super(name, price, categoria);
	}
	
	@Override
	public Double calculateDiscount() {
		if (price > 500) {
			return price*0.1;
		} else {
			return 0.0;
		}
	}
}
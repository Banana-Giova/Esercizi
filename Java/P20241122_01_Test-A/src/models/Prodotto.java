package models;

public abstract class Prodotto implements Comparable<Prodotto>{
	public String name;
	public double price;
	public String categoria;
	private double discounted_price;
	
	public Prodotto(String name, Double price, String categoria) {
		this.name = name;
		this.price = price;
		this.categoria = categoria;
		this.discounted_price = price - this.calculateDiscount();
	}
	
    @Override
    public int compareTo(Prodotto altro_prod) {
        return Double.compare(this.discounted_price, altro_prod.discounted_price);
    }
	
	public abstract Double calculateDiscount();
	
	public String toString() {
		return String.format("Nome: " + name + 
						   "\nPrezzo: " + (price - this.calculateDiscount()) + 
						   "\nCategoria: " + categoria);
	}
}
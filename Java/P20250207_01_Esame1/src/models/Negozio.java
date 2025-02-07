package models;
import java.util.HashMap;

public class Negozio {
	private String nome;
	protected HashMap<Integer, Prodotto> prodotti_vendita = new HashMap<Integer, Prodotto>();
	private int last_int = 1000;
	public String getNome() {
		return nome;
	}
	protected void setNome(String nome) {
		this.nome = nome;
	}
	
	public Negozio(String nome) {
		this.setNome(nome);
	}
	private int getLastInt() {
		this.last_int++;
		return this.last_int;
	}
	
	public void addProdotto(Prodotto prod) {	
		this.prodotti_vendita.put(this.getLastInt(), prod);
		System.out.printf("Aggiunto con successo il prodotto %s al database di %s!\n", 
						  prod.getNome(), this.getNome());
	}
	public void printProdotti() {
		if (this.prodotti_vendita.size() > 0) {
			System.out.printf("Nel database di %s sono disponibili %d prodotti, ecco la lista completa!\n┌────╴",
							  this.getNome(), this.prodotti_vendita.size());
			for (HashMap.Entry<Integer, Prodotto> entry : this.prodotti_vendita.entrySet()) {
				int key = entry.getKey();
				Prodotto value = entry.getValue();
				System.out.printf("\n│ Codice prodotto: %d\n", key);
				System.out.print(value.toString());
			}
			System.out.println("└────╴\n");
		} else {
			System.out.printf("Nessun prodotto nel database di %s!\n", this.getNome());
		}
	}
}

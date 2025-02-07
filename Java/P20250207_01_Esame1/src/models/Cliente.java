package models;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;

public class Cliente {
	private String id;
	private String nome;
	private String cognome;
	private String email;
	private String password;
	private double saldo;
	private List<Prodotto> prodotti_acquistati = new ArrayList<Prodotto>();
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCognome() {
		return cognome;
	}
	public void setCognome(String cognome) {
		this.cognome = cognome;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getId() {
		return id;
	}
	protected void setSaldo(double saldo) {
		if (saldo > 0) {
			this.saldo = saldo;
		} else {
			System.out.println("Impossibile impostare un saldo minore di 0!");
		}
	}
	public double getSaldo() {
		return saldo;
	}
	public void addToSaldo(double plus_saldo) {
		if (plus_saldo > 0) {
			this.saldo += plus_saldo;
			System.out.printf("Aggiunti %f€ al saldo di %s %s!\n",
							  plus_saldo, this.getNome(), this.getCognome());
		} else {
			System.out.println("Impossibile aggiungere al saldo un numero minore di 0!");
		}
	}
	protected void setNewId() {
        int length = 16;
		String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        
        SecureRandom random = new SecureRandom();
        StringBuilder randomString = new StringBuilder(length);
        
        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            randomString.append(characters.charAt(randomIndex));
        }
        String new_id = randomString.toString();
        
        if (IDChecker.validateID(new_id)) {
        	this.id = new_id;
        	return;
        } else {
        	this.setNewId();
        }
    }

	public Cliente(String nome, String cognome, String email, String password, double saldo) {
		this.setNewId();
		this.setNome(nome);
		this.setCognome(cognome);
		this.setEmail(email);
		this.setPassword(password);
		this.setSaldo(saldo);
	}
	
	public void printProdotti() {
		if (this.prodotti_acquistati.size() > 0) {
			System.out.printf("%s %s ha acquistato in totale %d prodotti sul nostro sito!\n┌────╴",
							  this.getNome(), this.getCognome(), this.prodotti_acquistati.size());
			for (Prodotto prodotto : this.prodotti_acquistati) {
				System.out.print("\n" + prodotto.toString());
			}
			System.out.println("└────╴");
		} else {
			System.out.printf("Nessun prodotto acquistato nella cronologia ordini di %s %s!\n", this.getNome(), this.getCognome());
		}
	}
	public void acquistaProdotto(Negozio negozio, int codice_prodotto) {
		if (negozio.prodotti_vendita.containsKey(codice_prodotto)) {
			if (this.getSaldo() >= negozio.prodotti_vendita.get(codice_prodotto).getPrezzo()) {
				this.setSaldo(this.getSaldo() - negozio.prodotti_vendita.get(codice_prodotto).getPrezzo());;
				this.prodotti_acquistati.add( negozio.prodotti_vendita.get(codice_prodotto));
				System.out.printf("Prodotto con codice %d acquistato da %s!\n",
								  codice_prodotto, negozio.getNome());
			} else {
				System.out.printf("Mi spiace %s %s! Non hai abbastanza soldi sul tuo conto! Saldo: %f, Prezzo prodotto: %f \n",
								  this.getNome(), this.getCognome(), this.getSaldo(), negozio.prodotti_vendita.get(codice_prodotto).getPrezzo());
			}
				
		} else {
			System.out.printf("Nessun prodotto da %s con codice %d!\n",
								negozio.getNome(), codice_prodotto);
		}
	}
}

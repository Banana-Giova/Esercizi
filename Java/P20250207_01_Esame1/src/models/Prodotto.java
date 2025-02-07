package models;
import java.security.SecureRandom;

public abstract class Prodotto {
	protected String id;
	protected String nome;
	protected String descrizione;
	protected double prezzo;
	
	public String getNome() {
		return nome;
	}
	protected void setNome(String nome) {
		this.nome = nome;
	}
	public String getDescrizione() {
		return descrizione;
	}
	protected void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}
	public double getPrezzo() {
		return prezzo;
	}
	protected void setPrezzo(double prezzo) {
		if (prezzo > 0) {
			this.prezzo = prezzo;
		} else {
			System.out.println("Impossibile impostare un prezzo minore di 0!");
		}
	}
	public String getId() {
		return id;
	}
	
	@Override
	public abstract String toString();
	
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
	
}

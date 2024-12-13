package models;

import java.util.*;

@SuppressWarnings("unused")
public class Agenzia {
	private String nome;
	private Map<String, CompagniaAerea> lista_compagnie;
	
	public Agenzia(String nome) {
		super();
		this.nome = nome;
		this.lista_compagnie = new HashMap<>();
	}
	
	public String getNome() {
		return nome;
	}
	private void setNome(String nome) {
		this.nome = nome;
	}
	
	private static void successo() {
		System.out.println("Operazione effettuata con successo!");
	}
	
	public void add_compagnia(CompagniaAerea compagnia) {
		if (!this.lista_compagnie.containsKey(compagnia.getNome())) {
			this.lista_compagnie.put(compagnia.getNome(), compagnia);
			successo();
		} else {
			throw new IllegalArgumentException("La compagnia fornita è già presente nella lista delle compagnie di questa agenzia.");
		}
	}
	
	public void mostra_compagnie() {
		if (this.lista_compagnie.size() > 0) {
			for (Map.Entry<String, CompagniaAerea> entry : this.lista_compagnie.entrySet()) {
				String ki = entry.getKey();
				System.out.println("Nome Compagnia: " + ki);
			}
		} else {
			System.out.println("Nessuna compagnia presente nella lista di questa agenzia.");
		}
	}
	
	public void remove_compagnia(String nome_comp) {
		if (this.lista_compagnie.containsKey(nome_comp)) {
			this.lista_compagnie.remove(nome_comp);
			successo();
		} else {
			throw new IllegalArgumentException("La compagnia fornita non è presente nella lista delle compagnie di questa agenzia.");
		}
	}
	
	public void prenota_volo(String nome_comp, String utente, Aeroporto aeroporto,
							 Volo volo, int posti_richiesti) {
		if (this.lista_compagnie.containsKey(nome_comp)) {
			try {
				this.lista_compagnie.get(nome_comp).prenota_volo(utente, aeroporto, volo, posti_richiesti);
				successo();
			} catch(Exception e) {
				throw new IllegalArgumentException(e);
			}
		} else {
			throw new IllegalArgumentException("La compagnia fornita non è presente nella lista delle compagnie di questa agenzia.");
		}
	}
	
	public void mostra_prenotazioni(String nome_comp, String utente) {
		if (this.lista_compagnie.containsKey(nome_comp)) {
			try {
				this.lista_compagnie.get(nome_comp).mostra_prenotazioni(utente);;
			} catch(Exception e) {
				throw new IllegalArgumentException(e);
			}
		} else {
			throw new IllegalArgumentException("La compagnia fornita non è presente nella lista delle compagnie di questa agenzia.");
		}
	}
	
	public void cancella_prenotazione(String nome_comp, String utente, String codice) {
		if (this.lista_compagnie.containsKey(nome_comp)) {
			try {
				this.lista_compagnie.get(nome_comp).cancella_prenotazione(utente, codice);
				successo();
			} catch(Exception e) {
				throw new IllegalArgumentException(e);
			}
		} else {
			throw new IllegalArgumentException("La compagnia fornita non è presente nella lista delle compagnie di questa agenzia.");
		}
	}
	
	
	
	
	
	
}

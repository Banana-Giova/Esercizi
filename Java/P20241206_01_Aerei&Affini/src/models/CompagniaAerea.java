package models;
import java.util.*;

@SuppressWarnings("unused")
public class CompagniaAerea {

	private String nome;
	private Map<String, Aereo> lista_aerei;
	private Map<String, Prenotazione> prenotazioni;
	
	public String getNome() {
		return nome;
	}

	private void setNome(String nome) {
		this.nome = nome;
	}

	public CompagniaAerea (String nome) {
		this.nome = nome;
	}
	
	public void crea_aereo(String codice, int posti) {
		try {
			if (!lista_aerei.containsKey(codice)) {
				Aereo new_aereo = new Aereo(codice, posti);
				lista_aerei.put(codice, new_aereo);
			}
			else {
				throw new IllegalArgumentException("L'aereo è già presente nella lista degli aerei.");
			}
		} catch(IllegalArgumentException e) {
			System.out.println(e);
		}
	}
	
	public void elimina_aereo(String codice) {
		if (lista_aerei.containsKey(codice)) {
			lista_aerei.remove(codice);
			System.out.printf("L'aereo con codice %d è stato eliminato dalla lista con successo.", codice);
		} else {
			System.out.printf("L'aereo con codice %d non è presente nella nostra lista di aerei.", codice);
		}
	}
	
	public void prenota_volo(String utente, Aeroporto aeroporto,
							 Volo volo, int posti_richiesti) {
		Prenotazione new_prenot = new Prenotazione(utente, posti_richiesti, volo);
		if (volo.getPartenza() == aeroporto && !prenotazioni.containsKey(new_prenot.getCodice())) {
			prenotazioni.put(new_prenot.getCodice(), new_prenot);
			volo.prenota_posti(posti_richiesti);
		} else {
			throw new IllegalArgumentException("L'aeroporto fornito non coincide con la partenza del volo selezionato.");
		}
	}
	
	public void mostra_prenotazioni(String utente) {
		boolean flag = false;
		for (Map.Entry<String, Prenotazione> entry : this.prenotazioni.entrySet()) {
			String ki = entry.getKey();
			Prenotazione vi = entry.getValue();
			if (vi.getUtente() == utente) {
				System.out.println("Codice: " + ki + ", Posti Richiesti: " + vi.getPosti_prenotati());
				flag = true;
			}
		if (flag == false) {
			System.out.println("Nessuna prenotazione rilevata a nome dell'utente selezionato.");
		}
		}
	}
	
	public void annulla_prenotazione(String utente, String codice) {
		if (this.prenotazioni.containsKey(codice) && this.prenotazioni.get(codice).getUtente() == utente) {
			Prenotazione da_annullare = this.prenotazioni.get(codice);
			
		} else {
			throw new IllegalArgumentException("E' impossibile annullare la prenotazione.");
		}
	}
}








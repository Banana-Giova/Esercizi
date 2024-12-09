package models;
import java.util.*;

@SuppressWarnings("unused")
public class CompagniaAerea {
	private String nome;
	private Map<String, Aereo> lista_aerei;
	private Map<String, Volo> lista_voli;
	private Map<String, Prenotazione> prenotazioni;
	
	public CompagniaAerea(String nome) {
		this.nome = nome;
		this.lista_aerei = new HashMap<>();
		this.lista_voli = new HashMap<>();
		this.prenotazioni = new HashMap<>();
	}
	
	public String getNome() {
		return nome;
	}

	private void setNome(String nome) {
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
	
	public void mostra_aerei() {
		if (this.lista_aerei.size() > 0) {
			for (Map.Entry<String, Aereo> entry : this.lista_aerei.entrySet()) {
				String ki = entry.getKey();
				Aereo vi = entry.getValue();
				System.out.println("Codice: " + ki + ", Posti Totali: " + vi.getPosti_totali());
			}
		} else {
			System.out.println("Nessun aereo presente nella lista di questa agenzia.");
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
	
	public void crea_volo(String codice, Aereo aereo, Aeroporto partenza, Aeroporto arrivo,
					 	  int d_giorno, int d_mese, int d_anno, int d_ora, int d_minuti,
						  int a_giorno, int a_mese, int a_anno, int a_ora, int a_minuti) {
		try {
			if (!lista_voli.containsKey(codice)) {
				Volo new_volo = new Volo(codice, aereo, this, partenza, arrivo,
									 d_giorno, d_mese, d_anno, d_ora, d_minuti,
									 a_giorno, a_mese, a_anno, a_ora, a_minuti);
				lista_voli.put(codice, new_volo);
			}
			else {
				throw new IllegalArgumentException("Il volo è già presente nella lista dei voli.");
			}
		} catch(IllegalArgumentException e) {
			System.out.println(e);
		}
	}
	
	public void mostra_voli() {
		if (this.lista_voli.size() > 0) {
			for (Map.Entry<String, Volo> entry : this.lista_voli.entrySet()) {
				String ki = entry.getKey();
				Volo vi = entry.getValue();
				System.out.println("Codice: " + ki + ", Aereo: " + vi.getAereo() +
								   ", \nAeroporto di Partenza: " + vi.getPartenza().getNome() +
								   ", Aeroporto di Arrivo: " + vi.getArrivo().getNome() +
								   ", \nStato del Volo: " + vi.getStato_volo() +
								   ", Decollo: " + vi.getDecollo() +
								   ", Atterraggio: " + vi.getAtterraggio() +
								   ", \nPosti Disponibili: " + vi.getPosti_disponibili());
			}
		} else {
			System.out.println("Nessun volo presente nella lista di questa compagnia.");
		}
	}
	
	public void elimina_volo(String codice) {
		if (lista_voli.containsKey(codice)) {
			lista_voli.remove(codice);
			System.out.printf("Il volo con codice %d è stato eliminato dalla lista con successo.", codice);
		} else {
			System.out.printf("Il volo con codice %d non è presente nella nostra lista di voli.", codice);
		}
	}
	
	public void prenota_volo(String utente, Aeroporto aeroporto,
							 Volo volo, int posti_richiesti) {
		Prenotazione new_prenot = new Prenotazione(utente, posti_richiesti, volo);
		if (volo.getPartenza() == aeroporto && !prenotazioni.containsKey(new_prenot.getCodice())) {
			prenotazioni.put(new_prenot.getCodice(), new_prenot);
			volo.prenota_posti(posti_richiesti);
		} else {
			throw new IllegalArgumentException("L'aeroporto fornito non coincide con la partenza del volo selezionato o è già inserito.");
		}
	}
	
	public void mostra_prenotazioni(String utente) {
		boolean flag = false;
		if (this.prenotazioni.size() > 0) {
			for (Map.Entry<String, Prenotazione> entry : this.prenotazioni.entrySet()) {
				String ki = entry.getKey();
				Prenotazione vi = entry.getValue();
				if (vi.getUtente() == utente) {
					System.out.println("Codice: " + ki + ", Posti Richiesti: " + vi.getPosti_prenotati());
					flag = true;
				}	
			}
		if (flag == false) {
			System.out.println("Nessuna prenotazione rilevata a nome dell'utente selezionato.");
			}
		}
	}
	
	public void annulla_prenotazione(String utente, String codice) {
		if (this.prenotazioni.containsKey(codice) && this.prenotazioni.get(codice).getUtente() == utente) {
			Prenotazione da_annullare = this.prenotazioni.get(codice);
			da_annullare.getVolo().annulla_prenotazione(da_annullare.getPosti_prenotati());
			this.prenotazioni.remove(codice);
		} else {
			throw new IllegalArgumentException("E' impossibile annullare la prenotazione.");
		}
	}
}

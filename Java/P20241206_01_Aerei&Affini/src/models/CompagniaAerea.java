package models;
import java.util.*;

import types.StatoVolo;

@SuppressWarnings("unused")
public class CompagniaAerea {
	private String nome;
	private Map<String, Aereo> lista_aerei;
	private Map<String, Volo> lista_voli;
	private Map<String, Prenotazione> prenotazioni;
	private Map<String, Aeroporto> lista_aeroporti;
	
	public CompagniaAerea(String nome) {
		super();
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
	
	private static void successo() {
		System.out.println("Operazione effettuata con successo!");
	}
	
    private static boolean isNotPartito(Volo volo) {
        Set<StatoVolo> statiValidi = new HashSet<>();
        statiValidi.add(StatoVolo.PIANIFICATO);
        statiValidi.add(StatoVolo.IN_ATTESA);

        return statiValidi.contains(volo.getStato_volo());
    }
    
	public void mostra_aeroporti() {
		if (this.lista_aeroporti.size() > 0) {
			System.out.println("Lista degli aeroporti a seguire\n\n-----\n");
			for (Map.Entry<String, Aeroporto> entry : this.lista_aeroporti.entrySet()) {
				String ki = entry.getKey();
				Aeroporto vi = entry.getValue();
				System.out.println("\nCodice: " + ki + ", Nome: " + vi.getNome());
				successo();
			}
		} else {
			System.out.println("Nessun aeroporto presente nella lista di questa compagnia.");
		}
	}
	
	public void add_aeroporto(Aeroporto aeroporto) {
		if (!this.lista_aeroporti.containsKey(aeroporto.getCodice())) {
			this.lista_aeroporti.put(aeroporto.getCodice(), aeroporto);
			successo();
		} else {
			throw new IllegalArgumentException("L'aeroporto fornito è già presente nella lista degli aeroporti di questa agenzia.");
		}
	}
	
	public void remove_aeroporto(String nome_comp) {
		if (this.lista_aeroporti.containsKey(nome_comp)) {
			this.lista_aeroporti.remove(nome_comp);
			successo();
		} else {
			throw new IllegalArgumentException("L'aeroporto fornito non è presente nella lista degli aeroporti di questa agenzia.");
		}
	}
	
	public void crea_aereo(String codice, int posti) {
		try {
			if (!this.lista_aerei.containsKey(codice)) {
				Aereo new_aereo = new Aereo(codice, posti);
				this.lista_aerei.put(codice, new_aereo);
				successo();
			}
			else {
				throw new IllegalArgumentException("L'aereo è già presente nella lista degli aerei.");
			}
		} catch(IllegalArgumentException e) {
			System.out.println(e);
		}
	}
	
	public void elimina_aereo(String codice) {
		if (this.lista_aerei.containsKey(codice)) {
			this.lista_aerei.remove(codice);
			System.out.printf("L'aereo con codice %d è stato eliminato dalla lista con successo.", codice);
		} else {
			System.out.printf("L'aereo con codice %d non è presente nella nostra lista di aerei.", codice);
		}
	}
	
	public void mostra_aerei() {
		if (this.lista_aerei.size() > 0) {
			System.out.println("Lista degli aerei a seguire\n\n-----\n");
			for (Map.Entry<String, Aereo> entry : this.lista_aerei.entrySet()) {
				String ki = entry.getKey();
				Aereo vi = entry.getValue();
				System.out.println("\nCodice: " + ki + ", Posti Totali: " + vi.getPosti_totali());
			}
		} else {
			System.out.println("Nessun aereo presente nella lista di questa compagnia.");
		}
	}
	
	protected void crea_volo(String codice, String codice_aereo, String codice_partenza, String codice_arrivo,
					 	  int decollo_giorno, int d_mese, int d_anno, int d_ora, int d_minuti,
						  int arrivo_giorno, int a_mese, int a_anno, int a_ora, int a_minuti) {
		if (!this.lista_voli.containsKey(codice) 
		  && this.lista_aerei.containsKey(codice_aereo)
		  && this.lista_aeroporti.containsKey(codice_partenza)
		  && this.lista_aeroporti.containsKey(codice_arrivo)) {
			Volo new_volo = new Volo(codice, this.lista_aerei.get(codice_aereo), this, 
								 this.lista_aeroporti.get(codice_partenza), 
								 this.lista_aeroporti.get(codice_arrivo),
								 decollo_giorno, d_mese, d_anno, d_ora, d_minuti,
								 arrivo_giorno, a_mese, a_anno, a_ora, a_minuti);
			this.lista_voli.put(codice, new_volo);
			this.lista_aeroporti.get(codice_partenza).add_volo(new_volo);
		}
	}
	
	public void mostra_voli() {
		if (this.lista_voli.size() > 0) {
			System.out.println("Lista dei voli a seguire\nN.B.: Possono essere prenotati solo voli PIANIFICATI o IN ATTESA!\n\n-----\n");
			for (Map.Entry<String, Volo> entry : this.lista_voli.entrySet()) {
				String ki = entry.getKey();
				Volo vi = entry.getValue();
				System.out.println("\nCodice: " + ki + ", Aereo: " + vi.getAereo() +
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
	
	protected void elimina_volo(String codice) {
		if (lista_voli.containsKey(codice)) {
			lista_voli.get(codice).getPartenza().remove_volo(lista_voli.get(codice));
			lista_voli.remove(codice);
			System.out.printf("Il volo con codice %d è stato eliminato dalla lista con successo.", codice);
		} else {
			System.out.printf("Il volo con codice %d non è presente nella nostra lista di voli.", codice);
		}
	}
	
	protected void prenota_volo(String utente, Aeroporto aeroporto,
							 Volo volo, int posti_richiesti) {
		Prenotazione new_prenot = new Prenotazione(utente, posti_richiesti, volo);
		if (volo.getPartenza() == aeroporto 
		&& !prenotazioni.containsKey(new_prenot.getCodice())
		&& CompagniaAerea.isNotPartito(volo)) {
			prenotazioni.put(new_prenot.getCodice(), new_prenot);
			volo.prenota_posti(posti_richiesti);
			successo();
		} else {
			throw new IllegalArgumentException("L'aeroporto fornito non coincide con la partenza del volo selezionato o è già inserito.");
		}
	}
	
	protected void mostra_prenotazioni(String utente) {
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
	
	protected void cancella_prenotazione(String utente, String codice) {
		if (this.prenotazioni.containsKey(codice) 
			&& this.prenotazioni.get(codice).getUtente() == utente) {
			Prenotazione da_annullare = this.prenotazioni.get(codice);
			if (CompagniaAerea.isNotPartito(da_annullare.getVolo())) {
				da_annullare.getVolo().annulla_prenotazione(da_annullare.getPosti_prenotati());
				this.prenotazioni.remove(codice);
				successo();
			} else {
				throw new IllegalArgumentException("Il volo non è in uno stato annullabile, puoi annullare una prenotazione solo su un volo ancora non completato.");
			}
		} else {
			throw new IllegalArgumentException("E' impossibile annullare la prenotazione.");
		}
	}
	
	public void mostra_tutte_prenotazioni() {
		if (this.prenotazioni.size() > 0) {
			System.out.println("Lista di tutte le prenotazioni associate a questa compagnia a seguire\n\n-----\n");
			for (Map.Entry<String, Prenotazione> entry : this.prenotazioni.entrySet()) {
				String ki = entry.getKey();
				Prenotazione vi = entry.getValue();
				System.out.println("\nCodice: " + ki + ", Nome: " + vi.getUtente() + ", Posti Prenotati: " + vi.getPosti_prenotati());
			}
		} else {
			System.out.println("Nessuna prenotazione presente nella lista di questa compagnia.");
		}
	}
	
	protected void modificaStatoVolo(String codice_volo, int request) {
		if (this.lista_voli.containsKey(codice_volo)) {
			this.lista_voli.get(codice_volo).setStato_volo(request);
			successo();
		} else {
			throw new IllegalArgumentException("Il volo fornito non fa parte dei voli della nostra compagnia.");
		}
	}
	
}

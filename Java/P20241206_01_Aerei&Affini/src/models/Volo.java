package models;
import java.time.*;
import types.*;

@SuppressWarnings("unused")
public class Volo {
	private String codice;
	private Aereo aereo;
	private CompagniaAerea comp;
	private Aeroporto aero_partenza;
	private Aeroporto aero_arrivo;
	private LocalDateTime decollo;
	private LocalDateTime atterraggio;
	private StatoVolo stato_volo;
	private int posti_occupati;
	private int posti_disponibili;
	
   public static boolean isValidDate(int giorno, int mese, int anno) {
        try {
            LocalDateTime.of(anno, mese, giorno, 0, 0);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public Aereo getAereo() {
	return this.aereo;
	}
	
	private void setAereo(Aereo aereo) {
		this.aereo = aereo;
	}
	
	public Aeroporto getPartenza() {
		return this.aero_partenza;
	}
	
	private void setPartenza(Aeroporto partenza) {
		this.aero_partenza = partenza;
	}
	
	public Aeroporto getArrivo() {
		return this.aero_arrivo;
	}
	
	private void setArrivo(Aeroporto arrivo) {
		this.aero_arrivo = arrivo;
	}
	
	public LocalDateTime getData_ora() {
		return this.decollo;
	}
	
	private void setData_ora(LocalDateTime data_ora) {
		this.decollo = data_ora;
	}
	
	public String getCodice() {
		return this.codice;
	}	
	
	public LocalDateTime getDecollo() {
		return this.decollo;
	}

	private void setDecollo(LocalDateTime decollo) {
		this.decollo = decollo;
	}
	
	public LocalDateTime getAtterraggio() {
		return this.atterraggio;
	}

	private void getAtterraggio(LocalDateTime atterraggio) {
		this.atterraggio = atterraggio;
	}

	public StatoVolo getStato_volo() {
		return this.stato_volo;
	}

	private void setStato_volo(String stato_volo) {
		this.stato_volo = StatoVolo.valueOf(stato_volo);
	}

	public static boolean isValidTime(int ora, int minuti) {
        return ora >= 0 && ora <= 23 && minuti >= 0 && minuti <= 59;
    }
	
	public int getPosti_occupati() {
		return this.posti_occupati;
	}
	
	public void setPosti_occupati(int posti_occupati) {
		this.posti_occupati = posti_occupati;
		this.update_posti_disponibili();
	}
	
	public int getPosti_disponibili() {
		this.update_posti_disponibili();
		return posti_disponibili;
	}
	
	private void update_posti_disponibili() {
		this.posti_disponibili = this.aereo.getPosti_totali() - this.posti_occupati;
	}
	
	public void prenota_posti(int numero_posti) {
		int post_prenotazione = this.posti_occupati + numero_posti;
		if (post_prenotazione < this.aereo.getPosti_totali()) {
			this.setPosti_occupati(post_prenotazione);
			this.update_posti_disponibili();
			System.out.println("Posti prenotati con successo.");
		} else {
			throw new IllegalArgumentException("Il numero di posti richiesti supera il numero di posti disponibili.");
		}
	}
	
	public void annulla_prenotazione(int numero_posti) {
		int post_prenotazione = this.posti_occupati - numero_posti;
		if (post_prenotazione > 0 ) {
			this.setPosti_occupati(post_prenotazione);
			this.update_posti_disponibili();
			System.out.println("Prenotazione annullata con successo.");
		} else {
			throw new IllegalArgumentException("Il numero di posti da annullare eccede il quantitativo possibile.");
		}
	}
	
	public Volo (String codice, Aereo aereo, CompagniaAerea comp,
				 Aeroporto partenza, Aeroporto arrivo,
				 int d_giorno, int d_mese, int d_anno, int d_ora, int d_minuti,
				 int a_giorno, int a_mese, int a_anno, int a_ora, int a_minuti) {
		this.codice = codice;
		this.aereo = aereo;
		this.comp = comp;
		this.aero_partenza = partenza;
		this.aero_arrivo = arrivo;
		this.posti_disponibili = aereo.getPosti_totali();
		this.posti_occupati = 0;
		this.stato_volo = StatoVolo.valueOf("PIANIFICATO");
		if (isValidDate(d_giorno, d_mese, d_anno) && isValidTime(d_ora, d_minuti)) {
			this.decollo = LocalDateTime.of(d_anno, d_mese, d_giorno, d_ora, d_minuti);
		} else {
			throw new IllegalArgumentException("L'orario e/o la data fornita per il decollo non sono validi.");
		}
		if (isValidDate(a_giorno, a_mese, a_anno) && isValidTime(a_ora, a_minuti)) {
			this.atterraggio = LocalDateTime.of(a_anno, a_mese, a_giorno, a_ora, a_minuti);
		} else {
			throw new IllegalArgumentException("L'orario e/o la data fornita per l'atterraggio non sono validi.");
		}
		if (this.atterraggio.isBefore(this.decollo)) {
			throw new IllegalArgumentException("L'orario e/o la data fornita per l'atterraggio sono precedenti al decollo!");
		}
	}
}

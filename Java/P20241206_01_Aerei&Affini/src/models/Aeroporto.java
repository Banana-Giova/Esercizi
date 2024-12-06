package models;

import java.util.Map;

@SuppressWarnings("unused")
public class Aeroporto {
	private String codice;
	private Map<String, Volo> partenze;
	
	public String getCodice() {
		return codice;
	}

	private void setCodice(String codice) {
		this.codice = codice;
	}
	
	public Aeroporto (String codice) {
		this.codice = codice;
	}
	
	public void add_volo(Volo volo) {
		if (!partenze.containsKey(volo.getCodice()) && volo.getPartenza() == this) {
			this.partenze.put(volo.getCodice(), volo);
		} else {
			throw new IllegalArgumentException("Il volo è già presente nella lista dei voli.");
		}
	}
	
	public void remove_volo(Volo volo) {
		if (partenze.containsKey(volo.getCodice())) {
			this.partenze.remove(volo.getCodice(), volo);
		} else {
			throw new IllegalArgumentException("Il volo non è presente nella lista dei voli.");
		}
	}
	
}

package models;
import java.util.*;

@SuppressWarnings("unused")
public class Aeroporto {
	private String codice;
	private String nome;
	private Map<String, Volo> partenze;
	
	public String getCodice() {
		return codice;
	}

	private void setCodice(String codice) {
		this.codice = codice;
	}
	
	public String getNome() {
		return nome;
	}

	private void setNome(String nome) {
		this.nome = nome;
	}
	
	public Aeroporto (String codice, String nome) {
		super();
		this.codice = codice;
		this.nome = nome;
		this.partenze = new HashMap<>();
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
	
	public void imbarcoVolo(String codice_volo) {
		if (partenze.containsKey(codice_volo)) {
			partenze.get(codice_volo).getComp().modificaStatoVolo(codice_volo, 3);
		} else {
			throw new IllegalArgumentException("Il volo non è presente nella lista dei voli.");
		}
	}
	
	public void decolloVolo(String codice_volo) {
		if (partenze.containsKey(codice_volo)) {
			partenze.get(codice_volo).getComp().modificaStatoVolo(codice_volo, 4);
		} else {
			throw new IllegalArgumentException("Il volo non è presente nella lista dei voli.");
		}
	}
	
	public void atterraggioVolo(String codice_volo) {
		if (partenze.containsKey(codice_volo)) {
			partenze.get(codice_volo).getComp().modificaStatoVolo(codice_volo, 7);
		} else {
			throw new IllegalArgumentException("Il volo non è presente nella lista dei voli.");
		}
	}
	
}

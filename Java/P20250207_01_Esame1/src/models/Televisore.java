package models;

public class Televisore extends Prodotto {
	private String marca;
	private int pollici;
	private boolean smart;
	
	public String getMarca() {
		return marca;
	}
	protected void setMarca(String marca) {
		this.marca = marca;
	}
	public int getPollici() {
		return pollici;
	}
	protected void setPollici(int pollici) {
		if (pollici > 0) {
			this.pollici = pollici;
		} else {
			System.out.println(("Impossibile impostare dei pollici minori di 0!"));
		}
	}
	public boolean isSmart() {
		return smart;
	}
	protected void setSmart(boolean smart) {
		this.smart = smart;
	}

	public Televisore(String nome, String descrizione, double prezzo, 
					 String marca, int pollici, boolean smart) {
		this.setNewId();
		this.setNome(nome);
		this.setDescrizione(descrizione);
		this.setPrezzo(prezzo);
		this.setMarca(marca);
		this.setPollici(pollici);;
		this.setSmart(smart);;
	}
	
    @Override
    public String toString() {
        String result = String.format("│ Televisore con ID '%s', Nome='%s', Descrizione='%s'\n│ Prezzo=%.2f, Marca='%s'\n│ Pollici=%d\", Smart Features=%b\n",
                id, nome, descrizione, prezzo, marca, pollici, smart);

        return result;
    }
}

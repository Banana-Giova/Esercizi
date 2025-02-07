package models;

public class Smartphone extends Prodotto {
	private String marca;
	private int ram;
	private int rom;
	private boolean microsd;
	
	public String getMarca() {
		return marca;
	}
	protected void setMarca(String marca) {
		this.marca = marca;
	}
	public int getRam() {
		return ram;
	}
	protected void setRam(int ram) {
		if (ram > 0) {
			this.ram = ram;
		} else {
			System.out.println(("Impossibile impostare una RAM minore di 0!"));
		}
	}
	public int getRom() {
		return rom;
	}
	protected void setRom(int rom) {
		if (rom > 0) {
			this.rom = rom;
		} else {
			System.out.println(("Impossibile impostare una ROM minore di 0!"));
		}
	}
	public boolean hasMicrosd() {
		return microsd;
	}
	protected void setMicrosd(boolean microsd) {
		this.microsd = microsd;
	}

	public Smartphone(String nome, String descrizione, double prezzo, 
					 String marca, int ram, int rom, boolean microsd) {
		this.setNewId();
		this.setNome(nome);
		this.setDescrizione(descrizione);
		this.setPrezzo(prezzo);
		this.setMarca(marca);
		this.setRam(ram);
		this.setRom(rom);
		this.setMicrosd(microsd);
	}
	
    @Override
    public String toString() {
        String result = String.format("│ Smartphone con ID '%s', Nome='%s', Descrizione='%s'\n│ Prezzo=%.2f, Marca='%s', RAM=%d GB\n│ ROM=%d GB, MicroSD=%b\n",
                id, nome, descrizione, prezzo, marca, ram, rom, microsd);

        return result;
    }
}

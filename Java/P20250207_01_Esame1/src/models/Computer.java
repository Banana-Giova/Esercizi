package models;

public class Computer extends Prodotto {
	private String marca;
	private int ram;
	private int rom;
	private int pollici;
	private boolean camera;
	private boolean microphone;
	
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
	public boolean hasCamera() {
		return camera;
	}
	protected void setCamera(boolean camera) {
		this.camera = camera;
	}
	public boolean hasMicrophone() {
		return microphone;
	}
	protected void setMicrophone(boolean microphone) {
		this.microphone = microphone;
	}
	
	public Computer(String nome, String descrizione, double prezzo, 
					 String marca, int ram, int rom, int pollici,
					 boolean camera, boolean microphone) {
		this.setNewId();
		this.setNome(nome);
		this.setDescrizione(descrizione);
		this.setPrezzo(prezzo);
		this.setMarca(marca);
		this.setRam(ram);
		this.setRom(rom);
		this.setPollici(pollici);
		this.setCamera(camera);
		this.setMicrophone(microphone);
	}
	
    @Override
    public String toString() {
        String result = String.format("│ Computer con ID con '%s', Nome='%s', Descrizione='%s'\n│ Prezzo=%.2f, Marca='%s', RAM=%d GB\n│ ROM=%d GB, Pollici=%d\n│ Telecamera=%b, Microfono=%b\n",
                id, nome, descrizione, prezzo, marca, ram, rom, pollici, camera, microphone);

        return result;
    }
}
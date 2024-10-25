import java.math.BigDecimal;
import java.math.RoundingMode;

public class Computer {

	private double prezzo;
	private double peso;
	private double larghezza;
	private double altezza;
	private double profondita;
	private double dimensioni;
	private String produttore;
	private int anno_produzione;
	public static int num_pc;
	
	private static int rangeRandint(int min, int max) {
	    return (int) ((Math.random() * (max - min)) + min);
	}
	
	static String[] produttori = {
			"Lenovo", "Apple", "Dell", 
			"Asus", "HP", "Razer",
			"Acer", "NZXT"
			};
	
	public int getAntiProduttore() {
		return 11-(this.getProduttore()).length();
	}
	
	public int getAntiLength(String nome) {
		
		if (nome == "prezzo") {
			return 14-((Double.toString(this.prezzo)).length());
		}
		if (nome == "peso") {
			return 16-((Double.toString(this.peso)).length());
		}
		if (nome == "larghezza") {
			return 10-((Double.toString(this.larghezza)).length());
		}
		if (nome == "altezza") {
			return 12-((Double.toString(this.altezza)).length());
		}
		if (nome == "profondita") {
			return 9-((Double.toString(this.profondita)).length());
		}
		if (nome == "dimensioni") {
			return 10-((Double.toString(this.dimensioni)).length());
		}
		else {
			return -100;
		}
	}
	
	private void UpdateDependents() {
	    BigDecimal dix = new BigDecimal(larghezza*altezza*profondita);
	    dix = dix.setScale(5, RoundingMode.FLOOR);
	    this.dimensioni = dix.doubleValue();
	}

	
	public double getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso = peso;
	}
	public double getLarghezza() {
		return larghezza;
	}
	public void setLarghezza(double larghezza) {
		this.larghezza = larghezza;
		UpdateDependents();
	}
	public double getAltezza() {
		return altezza;
	}
	public void setAltezza(double altezza) {
		this.altezza = altezza;
		UpdateDependents();
	}
	public double getProfondita() {
		return profondita;
	}
	public void setProfondita(double profondita) {
		this.profondita = profondita;
		UpdateDependents();
	}
	public String getProduttore() {
		return produttore;
	}
	public void setProduttore(String produttore) {
		this.produttore = produttore;
	}
	public int getAnno_produzione() {
		return anno_produzione;
	}
	public void setAnno_produzione(int anno_produzione) {
		this.anno_produzione = anno_produzione;
	}
	
	public double getDimensioni() {
		return dimensioni;
	}
	
	public String getPrintDimensioni() {
		String dipsy = Double.toString(dimensioni);
		return dipsy.substring(0, dipsy.length()-2);
	}
	
	public void newPC() {
		num_pc += 1;
	}
	
	public int getPCnum() {
		return num_pc;
	}
	
	public Computer(double prezzo, double peso, double larghezza, 
				    double altezza, double profondita, String produttore,
			        int anno_produzione) {
		super();
		this.prezzo = prezzo;
		this.peso = peso;
		this.larghezza = larghezza;
		this.altezza = altezza;
		this.profondita = profondita;
		this.produttore = produttore;
		this.anno_produzione = anno_produzione;
		
		UpdateDependents();
		newPC();
	}
	
	public static Computer generaRandPC() {
		return new Computer(
				Computer.rangeRandint(99, 9999)+0.99, Computer.rangeRandint(100, 5000), 
				Computer.rangeRandint(20, 50), Computer.rangeRandint(10, 50), 
				Computer.rangeRandint(1, 100), 
				Computer.produttori[Computer.rangeRandint(0, 8)], 
				Computer.rangeRandint(1995, 2024));
	}
	
}

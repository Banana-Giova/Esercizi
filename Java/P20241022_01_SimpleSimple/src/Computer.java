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
	
	private static double randomicTrunk(int numberofDecimals) {
		double new_x;
		while ( true ) {
		    BigDecimal x = new BigDecimal(Math.random());
		    x = x.setScale(numberofDecimals, RoundingMode.FLOOR);
		    new_x = x.doubleValue();
		    int x_len = Double.toString(new_x).length();
		    
		    if ( x_len == 7 ) {
		    	return new_x;
		    }
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
				Computer.randomicTrunk(5), Computer.randomicTrunk(5), 
				Computer.randomicTrunk(5), Computer.randomicTrunk(5), 
				Computer.randomicTrunk(5), "Lenovo", 
				(int) (Math.random() * 100));
	}
	
}

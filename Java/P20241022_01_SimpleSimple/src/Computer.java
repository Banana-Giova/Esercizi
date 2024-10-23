import java.math.BigDecimal;

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
	
	@SuppressWarnings("deprecation")
	private static double randomicTrunk(int numberofDecimals) {
		while ( true ) {
			double x = Math.random();
		    double new_x = (new BigDecimal(String.valueOf(x)).setScale(numberofDecimals, BigDecimal.ROUND_CEILING)).doubleValue();
		    if ( x != new_x ) {
		    	break;
		    }
		}
		return new_x;
	}
	
	private void UpdateDependents() {
		this.dimensioni = larghezza*altezza*profondita;
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
				Math.random(), Math.random(), 
				Math.random(), Math.random(), 
				Math.random(), "Lenovo", 
				(int) (Math.random() * 100));
	}
	
}

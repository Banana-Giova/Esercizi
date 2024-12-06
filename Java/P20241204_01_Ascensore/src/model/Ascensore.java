package model;

import java.util.Scanner;

public class Ascensore {

	private int curr_piano;
	private int piano_minimo;
	private int piano_massimo;
	private Scanner scan_pian;
	
	public Ascensore (int piano_minimo, int piano_massimo) {
		if (piano_minimo == piano_massimo) {
			throw new IllegalArgumentException("I piani minimo e massimo devono essere diversi.");
		} else if (piano_minimo > piano_massimo) {
			throw new IllegalArgumentException("Il piano minimo deve essere inferiore al piano massimo.");
		}
		this.piano_minimo = piano_minimo;
		this.piano_massimo = piano_massimo;
		this.curr_piano = 0;
		this.scan_pian = new Scanner(System.in);
	}
	
	private void spostamento_utente() {
		String movimento = "";
		int diff_piani = 0;
		
		System.out.println("A che piano vorrebbe andare?");
		int piano_utente = this.scan_pian.nextInt();
		
		if (piano_utente == this.curr_piano) {
			System.out.println("Lei è già al piano richiesto! Desidera spostarsi ancora?(Y/n)");
		}
		else if (piano_utente > this.piano_massimo || piano_utente < this.piano_minimo) {
			System.out.println("Impossibile, questo edificio va dal piano " + this.piano_minimo + 
					   " al piano " + this.piano_massimo + "!\nDesidera ancora spostarsi?(Y/n)");
		}
		else {
			if (piano_utente > this.curr_piano ) {
				movimento = "sale";
				diff_piani = piano_utente - this.curr_piano;
			}
			else {
				movimento = "scende";
				diff_piani = this.curr_piano - piano_utente;
			}
			System.out.println("Dal piano " + this.curr_piano +
					 		   " l'ascensore " + movimento +
					 		   " per " + diff_piani + 
					 		   ((diff_piani > 1)? " piani." : " piano."));
			this.curr_piano = piano_utente;
			System.out.println("E' giunto a destinazione, desidera spostarsi ancora?(Y/n)");
		}
		while (true){
			String scelta_utente = this.scan_pian.next();
			if (scelta_utente.equalsIgnoreCase("Y")) {
				this.spostamento_utente();
				break;
			}
			else if (scelta_utente.equalsIgnoreCase("N")) {
				System.out.println("Grazie per aver scelto il nostro ascensore, buona giornata!");
				this.scan_pian.close();
				break;
			}
			System.out.println("La sua selezione non è valida, è pregato di digitare 'Y' oppure 'n'.");
		}
	}
	
	public void chiamata() {
		String movimento;
		int diff_piani = 0;
		System.out.println("A che piano ti trovi? ");
		
		int piano_utente = this.scan_pian.nextInt();
		if (piano_utente > this.piano_massimo || piano_utente < this.piano_minimo) {
			System.out.println("Impossibile, questo edificio va dal piano " + this.piano_minimo + 
							   " al piano " + this.piano_massimo + "!");
			this.chiamata();
		}
		else if (piano_utente == this.curr_piano) {
			System.out.println("L'ascensore è già presente al vostro piano!");
			this.spostamento_utente();
		}
		else {
			if (piano_utente > this.curr_piano ) {
				movimento = "sale";
				diff_piani = piano_utente - this.curr_piano;
			}
			else {
				movimento = "scende";
				diff_piani = this.curr_piano - piano_utente;
			}
			System.out.println("Dal piano " + this.curr_piano +
					 		   " l'ascensore " + movimento +
					 		   " per " + diff_piani + 
					 		   ((diff_piani > 1)? " piani." : " piano."));
			this.curr_piano = piano_utente;
			this.spostamento_utente();
		}
	}
}

package model;

import java.util.Scanner;

public class Ascensore {
	/*
	Siamo in un palazzo di 3 piani e dobbiamo gestire i movimenti di un ascensore
	l'ascensore può andare verso l'alto e verso il basso di uno o più piani
	quindi i movimenti dell'ascensore non sono assoluti ma sono relativi:
	sali di un piano
	scendi di tre piani
	sali di due piani
	ecc.
	
	Scrivere un programma JAVA che ha un menu che consente all'utente di
	1) chiama l'ascensore
	2) vai al terzo piano (o k-esimo piano)
	Il programma dovrà stampare a schermo gli spostamenti relativi dell'ascensore.
	Esempio:
	- all'inizio l'ascensore, per inizializzazione, sta al piano terra (0)
	- se io sto al secondo piano e chiamo l'ascensore, questo stampa
	    - sto andando da piano 0 verso l'alto per due piani.
	- se ora io premo il bottone (1) l'ascensore stampa
	    - sto andando da piano 2 verso il basso di 1 piano
	e così via.
	Quindi l'input per l'ascensore è: 
	    - chiamata dal piano N (0, 1, 2, 3)
	    - spostati al piano K (0,1,2,3)*/
	
	private int curr_piano;
	private int piano_minimo;
	private int piano_massimo;
	
	public Ascensore (int piano_minimo, int piano_massimo) {
		if (piano_minimo != piano_massimo) {
			this.piano_minimo = piano_minimo;
			this.piano_massimo = piano_massimo;
		}
		this.curr_piano = 0;
	}
	
	private void spostamento_utente() {
		Scanner scan_pian = new Scanner(System.in);
		String movimento = "";
		int diff_piani = 0;
		
		System.out.println("A che piano vorrebbe andare?");
		int piano_utente = scan_pian.nextInt();
		
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
			String scelta_utente = scan_pian.next();
			if (scelta_utente.equals("Y") || scelta_utente.equals("y")) {
				this.spostamento_utente();
				break;
			}
			else if (scelta_utente.equals("n") || scelta_utente.equals("N")) {
				System.out.println("Grazie per aver scelto il nostro ascensore, buona giornata!");
				break;
			}
			System.out.println("La sua selezione non è valida, è pregato di digitare 'Y' oppure 'n'.");
		}
	}
	
	public void chiamata() {
		Scanner scan_pian = new Scanner(System.in);
		String movimento = "";
		int diff_piani = 0;
		System.out.println("A che piano ti trovi? ");
		
		int piano_utente = scan_pian.nextInt();
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

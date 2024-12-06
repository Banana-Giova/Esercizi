package main;
import model.*;

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


public class Main {
	public static void main(String[] args) {
		Ascensore lo_scenzore = new Ascensore(0, 3);
		lo_scenzore.chiamata();
	}
}

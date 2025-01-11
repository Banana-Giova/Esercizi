package models;

public class Cliente implements Runnable {
	
	public void run() {
		Thread.currentThread().setName(String.valueOf(ListaNumeri.getCountClienti()));
		try {
			Thread.sleep(ListaNumeri.getRandInt());
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		/*Thread.currentThread().setName(String.valueOf(ListaNumeri.getCountClienti()));
		
		Se si vuole che i clienti siano numerati in ordine di completamento e non in ordine
		di arrivo alla cassa, rimuovere il setName() a riga 6 ed utilizzare quello a riga 12*/
		System.out.println("Il cliente numero " 
						  + (Thread.currentThread().getName())
						  + " è stato servito!");
	}
	
}

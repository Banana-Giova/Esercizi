package models;

public class Cliente implements Runnable {
	
	@Override
	public void run() {
		try {
			Thread.sleep(ListaNumeri.getRandInt());
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("Il cliente a nome " + Thread.currentThread().getName() + " è stato servito!");
	}
	
}

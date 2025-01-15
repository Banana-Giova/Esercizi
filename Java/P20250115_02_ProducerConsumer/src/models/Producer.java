package models;
import java.util.*;

public class Producer implements Runnable {
	private final List<Integer> bufferCondiviso;
	private final int size;
	private Random random = new Random();
 
	public Producer(List<Integer> bufferCondiviso, int size) {
		this.bufferCondiviso = bufferCondiviso;
		this.size = size;
	}
	
	private void produce() {
		if (bufferCondiviso.size() < size) {
			synchronized (bufferCondiviso) {
				bufferCondiviso.add(random.nextInt(100));
				System.out.println("Produzione completata, numero di oggetti nel buffer: " + this.bufferCondiviso.size());
			}
		} else {
			System.out.println("Limite buffer raggiunto, da svuotare!");
		}
	}
	
	@Override
	public void run() {
		while(true) {
			try {
				produce();
				Thread.sleep(1000);
				
			} catch (InterruptedException ex) {
				ex.printStackTrace();
			}
		}
	}
}

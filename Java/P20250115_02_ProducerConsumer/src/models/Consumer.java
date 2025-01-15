package models;
import java.util.List;

public class Consumer implements Runnable {
	private final List<Integer> bufferCondiviso;
	private final int size;
 
	public Consumer(List<Integer> bufferCondiviso, int size) {
		this.bufferCondiviso = bufferCondiviso;
		this.size = size;
	}
	
	private void consume() {
		if (bufferCondiviso.size() == size) {
			synchronized (bufferCondiviso) {
				bufferCondiviso.clear();
				System.out.println("Limite raggiunto! Buffer svuotato");
			}
		}
	}
	
	@Override
	public void run() {
		try {
			while (true) {
				consume();
				Thread.sleep(500);
			}
		} catch (InterruptedException ex) {
			ex.printStackTrace();
		}
	}
}

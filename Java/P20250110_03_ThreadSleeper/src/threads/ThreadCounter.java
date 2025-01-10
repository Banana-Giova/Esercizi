package threads;

public class ThreadCounter implements Runnable {
	
	@Override
	public void run() {
		for (int i = 1; i < 6; i++) {
			System.out.println("ID: " + Thread.currentThread().getName() + " => " + i);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				System.out.println("Thread con ID " + Thread.currentThread().getName() + " interrote per via del seguente errore:");
				e.printStackTrace();
			};
		}
		
	}
	
}

package threads;

public class ThreadCounter implements Runnable {
	
	@Override
	public void run() {
		for (int i = 1; i < 6; i++) {
			System.out.println("ID: " + Thread.currentThread().getName() + " => " + i);
		}
		
	}
	
}

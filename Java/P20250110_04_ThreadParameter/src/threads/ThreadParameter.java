package threads;

public class ThreadParameter implements Runnable {
	private boolean ternary;
	
	private void ternary_true() {
		for (int i = 1; i < 11; i++) {
			System.out.println("ID: " + Thread.currentThread().getName() + " => " + i);
		}
	}
	
	private void ternary_false() {
		for (int i = 100; i > 89; i--) {
			System.out.println("ID: " + Thread.currentThread().getName() + " => " + i);
		}
	}
	
	public ThreadParameter(boolean ternary) {
		this.ternary = ternary;
	}
	
	@Override
	public void run() {
		if (this.ternary) {
			this.ternary_true();
		} else {
			this.ternary_false();
		}
	}
	
}

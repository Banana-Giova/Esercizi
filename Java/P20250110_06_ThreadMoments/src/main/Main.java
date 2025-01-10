package main;
import threads.*;

public class Main {

	public static void main(String[] args) {
		Thread t1 = new Thread(new ThreadCounter());
		Thread t2 = new Thread(new ThreadCounter());
		ThreadChecker trust = new ThreadChecker();
		
		trust.thread_state(t1);
		trust.thread_state(t2);
		
		t1.start();
		t2.start();
		
		trust.thread_state(t1);
		trust.thread_state(t2);
		
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		trust.thread_state(t1);
		trust.thread_state(t2);
	}
}

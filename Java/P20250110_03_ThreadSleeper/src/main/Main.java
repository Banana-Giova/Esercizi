package main;
import threads.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) {
		ExecutorService executor = new ThreadPoolExecutor(
			2, 2, 60, TimeUnit.SECONDS, new LinkedBlockingQueue<>()	
		);
	
		ThreadCounter t1 = new ThreadCounter();
		ThreadCounter t2 = new ThreadCounter();
		
		executor.submit(t1);
		executor.submit(t2);
		
		executor.shutdown();
	}

}

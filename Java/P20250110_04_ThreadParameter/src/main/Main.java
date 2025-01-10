package main;
import threads.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) {
		
		ExecutorService executor = new ThreadPoolExecutor(
			2, 2, 90, TimeUnit.SECONDS, new LinkedBlockingQueue<>()
		);
		ThreadParameter t1 = new ThreadParameter(true);
		ThreadParameter t2 = new ThreadParameter(false);
	
		executor.submit(t1);
		executor.submit(t2);
		
		executor.shutdown();
	}

}
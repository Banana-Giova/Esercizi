package main;
import models.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) {
		LinkedBlockingQueue<Posta> casella = new LinkedBlockingQueue<Posta>(10);
		
		Thread t1 = new Thread(new MandaPosta(casella));
		Thread t2 = new Thread(new LeggiPosta(casella));
		
		@SuppressWarnings("resource")
		ExecutorService executor = new ThreadPoolExecutor(2, 4, 1000, 
														  TimeUnit.MINUTES, 
														  new LinkedBlockingQueue<>(10));
		
		executor.submit(t1);
		executor.submit(t2);
	}

}

package main;
import models.*;
import java.util.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		List<Integer> lista1 = new ArrayList<Integer>();
		List<Integer> lista2 = new ArrayList<Integer>();
		DontStarve t1 = new DontStarve(lista1, lista2);
		DontStarve t2 = new DontStarve(lista2, lista1);
		
		ExecutorService executor = new ThreadPoolExecutor(2, 2, 5, TimeUnit.SECONDS, new LinkedBlockingQueue<>());
		executor.submit(t1);
		executor.submit(t2);
		executor.awaitTermination(5, TimeUnit.SECONDS);
		executor.close();
		System.out.println("Starvation terminata.");
	}
}

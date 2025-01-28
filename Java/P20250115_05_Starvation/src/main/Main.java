package main;
import models.*;
import java.util.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) throws Exception {
		List<Integer> lista1 = new ArrayList<Integer>();
		List<Integer> lista2 = new ArrayList<Integer>();
		
		ExecutorService executor = Executors.newFixedThreadPool(2);
		Future<?> future1 = executor.submit(new DontStarve(lista1, lista2));
		Future<?> future2 = executor.submit(new DontStarve(lista2, lista1));

		try {
			System.out.println("Thread partiti!");
			System.out.println(future1.get(5, TimeUnit.SECONDS) + "\n" + future2.get(5, TimeUnit.SECONDS));
		} catch (TimeoutException e) {
			future1.cancel(true);
			future2.cancel(true);
			System.out.println("Starvation terminata.");
			System.exit(0);
		}
	}
}

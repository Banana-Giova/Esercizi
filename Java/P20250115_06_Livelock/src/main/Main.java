package main;

import models.*;
import java.util.concurrent.*;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		Threadlock t1 = new Threadlock(null, "Thread1");
		;
		Threadlock t2 = new Threadlock(t1, "Thread1");
		t1 = new Threadlock(t2, "Thread2");
		ExecutorService executor = new ThreadPoolExecutor(2, 2, 5, TimeUnit.SECONDS,
				new LinkedBlockingQueue<Runnable>());

		executor.submit(t1);
		executor.submit(t2);
	}
}

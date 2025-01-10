package models;
import java.util.concurrent.*;

public class Bancone {
	private ExecutorService executor;
	
	private ExecutorService create_salumeria() {
		return new ThreadPoolExecutor(
				3, 30, 300, TimeUnit.SECONDS, 
				new LinkedBlockingQueue<>()
			);
	}
	
	public void salumeria_aperta() {
		this.executor = create_salumeria();
		for (int i = 0; i < 30; i++) {
			this.executor.submit(new Cliente());
		}
		this.executor.shutdown();
        try {
            if (!this.executor.awaitTermination(180, TimeUnit.SECONDS)) {
                System.out.println("Timeout raggiunto, forzando la terminazione.");
                this.executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            System.out.println("Attesa interrotta, forzando la terminazione.");
            this.executor.shutdownNow();
        }

        // Dopo che tutti i task sono stati completati
        System.out.println("Clienti tutti serviti!");
	}
}
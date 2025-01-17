package models;
import java.util.*;

public class DontStarve extends Thread {
	private List<Integer> lista;
	private List<Integer> counter_lista;
	
	public DontStarve(List<Integer> lista, List<Integer> counter_lista) {
		this.lista = lista;
		this.counter_lista = counter_lista;
	}
	
	private void test() {
		System.out.println("Niente deadlock!");
	}
	
	@Override
	public void run() {
		
			synchronized (lista) {
				System.out.println("Iniziato thread a ID " + Thread.currentThread().getName());
		         try {
		             Thread.sleep(100);
		           } catch (InterruptedException e) {
		             e.printStackTrace();
		           }
				synchronized (counter_lista) {
					counter_lista.add(1);
				}}
		test();
	}
}

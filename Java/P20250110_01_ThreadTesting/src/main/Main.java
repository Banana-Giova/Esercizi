package main;
import threads.*;

public class Main {

	public static void main(String[] args) {
		ThreadExtend text = new ThreadExtend();
		
		Thread trun = new Thread(new ThreadRunnable());
	
		text.start();
		trun.start();
	}
}

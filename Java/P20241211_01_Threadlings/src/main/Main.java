package main;
import threads.*;

public class Main {

	public static void main(String[] args) {
	        MyThread th1 = new MyThread(1000);
	        th1.start();

	        MyThread th2 = new MyThread(1000);
	        th2.start();
	}
}

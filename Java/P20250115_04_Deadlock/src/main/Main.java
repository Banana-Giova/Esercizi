package main;
import models.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		List<Integer> lista1 = new ArrayList<Integer>();
		List<Integer> lista2 = new ArrayList<Integer>();
		Threadlock t1 = new Threadlock(lista1, lista2);
		Threadlock t2 = new Threadlock(lista2, lista1);
		
		t1.start();
		t2.start();
	}
}

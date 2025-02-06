package models;


public class Automobile {
	public int velocita = 100;

	public int accelera(int velocita) {
		return velocita + 10;
	}

	public int decelera(int velocita) {
		return velocita - 10;
	}

	public int frena(int velocita) {
		return 0;
	}

	public int parti(int velocita) {
		return velocita + 10;
	}

}
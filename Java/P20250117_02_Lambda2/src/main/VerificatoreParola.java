package main;

@FunctionalInterface
interface VerificatoreParola {

	boolean verifica(String parola, int lunghezza);

}
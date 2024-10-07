
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*Esercizio 2:
		 * 
		*Dato un triangolo rettangolo i cui cateti misurano 
		**rispettivamente 45.3 e 67.2 metri:
		*
		*1) calcolare e stampare la lunghezza dell'ipotenusa
		*2) calcolare e stampare la sua area
		*3) calcolare e stampare il suo perimetro
		*4) Infine stampare circonferenza e area di un cerchio 
		*   di raggio pari ai 3/4 dell'ipotenusa.
		*
		*NB: In java per la radice quadrata utilizzare 
		*Math.sqrt(x). Se Math viene mostrato sottolineato, 
		*andare con il mouse su Math e selezionare la import 
		*della libreria
		*/
		double c1 = 45.3;
		double c2 = 67.2;
		double ipo = Math.sqrt((c1*c1) + (c2*c2));
		System.out.println("L'ipotenusa equivale a: " + ipo);
		double areat = (c1+c2)/2;
		double perit = c1+c2+ipo;
		System.out.println("L'area del triangolo equivale a: "+ areat);
		System.out.println("Il perimetro del triangolo equivale a: " + perit);
		double ray = ipo*(3/4);
		double areac = 2*Math.PI*ray;
		double halfperic = Math.PI*ray;
		double peric = halfperic * halfperic;
		System.out.println("L'area del cerchio equivale a: "+ areac);
		System.out.println("Il perimetro del cerchio equivale a: " + peric);
	}

}

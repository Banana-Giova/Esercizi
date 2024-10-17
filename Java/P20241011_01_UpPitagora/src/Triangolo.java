
public class Triangolo {
		// TODO Auto-generated method stub

		/*Esercizio 3:
		 * Rielabora l'esercizio usando getter e setter

		double c1 = 45.3;
		double c2 = 67.2;
		double ipo = Math.sqrt((c1*c1) + (c2*c2));
		System.out.println("L'ipotenusa equivale a: " + ipo);
		double areat = (c1*c2)/2;
		double perit = c1+c2+ipo;
		System.out.println("L'area del triangolo equivale a: "+ areat);
		System.out.println("Il perimetro del triangolo equivale a: " + perit);
		double ray = (ipo*3)/4;
		double areac = Math.PI*(ray*ray);
		double peric = 2*Math.PI*ray;
		System.out.println("L'area del cerchio equivale a: "+ areac);
		System.out.println("Il perimetro del cerchio equivale a: " + peric);
		*/
		
		private double cat1;
		private double cat2;
		private double hyp;
		private double area;
		private double perimetro;
		
		private void UpdateDependents() {
			hyp = Math.sqrt(cat1*cat1+cat2*cat2);
			area = (cat1*cat2)/2;
			perimetro = cat1+cat2+hyp;
		}
		
		public double getCat1() {
			return cat1;
		}
		public void setCat1(double cat1) {
			this.cat1 = cat1;
			UpdateDependents();
		}
		public double getCat2() {
			return cat2;
		}
		public void setCat2(double cat2) {
			this.cat2 = cat2;
			UpdateDependents();
		}
		public double getHyp() {
			return hyp;
		}
		public double getArea() {
			return area;
		}
		public double getPerimetro() {
			return perimetro;
		}
		
		public Triangolo(double cat1, double cat2) {
			super();
			this.cat1 = cat1;
			this.cat2 = cat2;
			
			UpdateDependents();
		}
	}
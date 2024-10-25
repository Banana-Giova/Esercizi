
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Computer comp0 = Computer.generaRandPC();
		Computer comp1 = Computer.generaRandPC();
		Computer comp2 = Computer.generaRandPC();
		Computer comp3 = Computer.generaRandPC();
		Computer comp4 = Computer.generaRandPC();
		Computer comp5 = Computer.generaRandPC();
		Computer comp6 = Computer.generaRandPC();
		Computer comp7 = Computer.generaRandPC();
		Computer comp8 = Computer.generaRandPC();
		Computer comp9 = Computer.generaRandPC();

		Computer[] objArray = new Computer[10];
		
		objArray[0] = comp0;
		objArray[1] = comp1;
		objArray[2] = comp2;
		objArray[3] = comp3;
		objArray[4] = comp4;
		objArray[5] = comp5;
		objArray[6] = comp6;
		objArray[7] = comp7;
		objArray[8] = comp8;
		objArray[9] = comp9;
		
		for (int i = 0; i<10; i++) {
			System.out.println("┌" + "─".repeat(24) + "┐");
			System.out.println("│ " + "Info PC sul numero " + i + ":  │\n├" + "─".repeat(24) + "┤");
			System.out.println("│ Prezzo:" + " ".repeat(objArray[i].getAntiLength("prezzo")) + objArray[i].getPrezzo() + "€ │");
			System.out.println("│ Peso:" + " ".repeat(objArray[i].getAntiLength("peso")) + objArray[i].getPeso() + "g │");
			System.out.println("│ Larghezza:" + " ".repeat(objArray[i].getAntiLength("larghezza")) + objArray[i].getLarghezza() + "cm │");
			System.out.println("│ Altezza:" + " ".repeat(objArray[i].getAntiLength("altezza")) + objArray[i].getAltezza() + "cm │");
			System.out.println("│ Profondità:" + " ".repeat(objArray[i].getAntiLength("profondita")) + objArray[i].getProfondita() + "cm │");
			System.out.println("│ Dimensioni:" + " ".repeat(objArray[i].getAntiLength("dimensioni")) + objArray[i].getPrintDimensioni() + "cm³ │");
			System.out.println("│ Produttore:" + " ".repeat(objArray[i].getAntiProduttore()) + objArray[i].getProduttore() + " │");
			System.out.println("│ Anno Produzione:  " + objArray[i].getAnno_produzione() + " │");
			System.out.println("└" + "─".repeat(24) + "┘");
			
		}
	}

}

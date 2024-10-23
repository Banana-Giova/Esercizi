
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
			System.out.println(objArray[i].getPrezzo());
		}
	}

}

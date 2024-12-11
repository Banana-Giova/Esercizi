package app;
import java.util.*;

public interface InputChecker {
	Scanner input_reader = new Scanner(System.in);
	
	public static boolean optionsCheckerNoAB(int input, int... args) {
		boolean flag = false;
		for (int arg : args) {
			if (input == arg) {
				flag = true;
				break;
			}
		}
		System.out.println("Input invalido. Si è pregati di ritornare uno dei seguenti numeri:");
		for (int numero : args) {
			System.out.print(numero + ") ");
		}
		return flag;
	}
	
	//slower
	public static boolean optionsCheckerWAB(int input, Integer... args) {
		if (Arrays.asList(args).contains(input)) {
			return true;
		} else {
			return false;
		}
	}
	
	public static int intInput() {
		int counter = 0;
		while (counter < 10) {
			counter ++;
			if (input_reader.hasNextInt()) {
				int new_input = input_reader.nextInt();
				return new_input;
			} else {
				System.out.printf("Input invalido, si è pregati di inserire un valore intero. (%d)\n", (10-counter));
				input_reader.next();
			}
		}
		System.out.println("Superato il limite di 10 tentativi errati, chiusura del programma in corso");
		System.exit(0);
		return -1;
	}
	
	
	
	
	public static int intInputWCheck(int... args) {
		int user_int = intInput();
		if (optionsCheckerNoAB(user_int, args)) {
			return user_int;
		} else {
			return intInputWCheck(args);
		}
	}
	
	public static void closeScanner() {
		input_reader.close();
	}
}

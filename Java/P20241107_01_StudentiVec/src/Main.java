import java.util.Scanner;

public class Main {
    private static final int INSERISCI = 1;
    private static final int STAMPA = 2;
    private static final int ESCI = 3;
    private static final int MAX_STU = 10;

    public static void main(String[] args) {
        Studente[] studenti = new Studente[MAX_STU];
        Scanner scanner = new Scanner(System.in);
        int count = 0;

        while (true) {
            mostraMenu();
            int scelta = scanner.nextInt();

            switch (scelta) {
                case INSERISCI:
                    count = aggiungiStudente(scanner, studenti, count);
                    break;
                case STAMPA:
                    stampaListaStudenti(studenti, count);
                    break;
                case ESCI:
                    scanner.close();
                    System.out.println("Arrivederci!");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Errore.");
            }
        }
    }

	    private static void mostraMenu() {
	        System.out.println("Selezionare un'operazione.\n");
	        System.out.println("\t1 => ADD\nInserisci uno studente (MAX 10)\n");
	        System.out.println("\t2 => PRINT\nStampa la lista degli studenti\n");
	        System.out.println("\t3 => EXIT\nEsci dal programma");
	    }
	
	    private static int aggiungiStudente(Scanner scanner, Studente[] studenti, int count) {
	        if (count >= studenti.length) {
	            System.out.println("Spazio insufficiente!");
	        } else {
	            System.out.print("Inserire nome: ");
	            String nome = scanner.next();
	            System.out.print("Inserire età: ");
	            int eta = scanner.nextInt();
	            System.out.print("Inserire corso: ");
	            String corso = scanner.next();
	            System.out.print("Inserire numero di matricola: ");
	            int numeroMatricola = scanner.nextInt();
	
	            studenti[count] = new Studente(nome, eta, corso, numeroMatricola);
	            count++;
	            System.out.println("Studente inserito con successo!");
	        }
	        return count;
	    }
	
	    private static void stampaListaStudenti(Studente[] studenti, int count) {
	        if (count == 0) {
	            System.out.println("Nessuno studente inserito!");
	        } else {
	            for (int i = 0; i < count; i++) {
	                System.out.println("Studente Nᵒ" + (i + 1) + ":\n" + studenti[i]);
            }
        }
    }
}
package models;
import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Calcolatrice {

	public static Logger logger = Logger.getLogger(Calcolatrice.class.getName());
	
	static {
		logger.setUseParentHandlers(false);
		ConsoleHandler handler = new ConsoleHandler();
		handler.setLevel(Level.ALL);
        logger.addHandler(handler);
        logger.setLevel(Level.ALL);
	}
	
	public static int somma (int a, int b) {
        logger.fine("Inizio operazione somma");
        int risultato = a + b;
        logger.info("Somma eseguita: " + a + " + " + b + " = " + risultato);
        return risultato;
	}
	public static int sottrazione (int a, int b) {
        logger.fine("Inizio operazione sottrazione");
        int risultato = a - b;
        logger.info("Sottrazione eseguita: " + a + " - " + b + " = " + risultato);
        return risultato;
	}
	public static int moltiplicazione (int a, int b) {
        logger.fine("Inizio operazione moltiplicazione");
        int risultato = a * b;
        logger.info("Moltiplicazione eseguita: " + a + " x " + b + " = " + risultato);
        return risultato;
	}
	public static double divisione (int a, int b) {
        logger.fine("Inizio operazione divisione");
        double risultato = (double)a/(double)b;
        logger.info("Divisione eseguita: " + a + " : " + b + " = " + risultato);
        return risultato;
	}
}

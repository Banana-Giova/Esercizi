package models;
import org.apache.logging.log4j.*;

public class Calcolatrice {
	private static Logger log4jlogger = LogManager.getLogger(Calcolatrice.class.getName());
	
	public static int somma (int a, int b) {
        log4jlogger.debug("Inizio operazione somma");
        int risultato = a + b;
        log4jlogger.info("Somma eseguita: {} + {} = {}", a, b, risultato);
        return risultato;
	}
	public static int sottrazione (int a, int b) {
		log4jlogger.debug("Inizio operazione sottrazione");
        int risultato = a - b;
        log4jlogger.info("Sottrazione eseguita: {} - {} = {}", a, b, risultato);
        return risultato;
	}
	public static int moltiplicazione (int a, int b) {
		log4jlogger.debug("Inizio operazione moltiplicazione");
        int risultato = a * b;
        log4jlogger.info("Moltiplicazione eseguita: {} x {} = {}", a, b, risultato);
        return risultato;
	}
	public static double divisione (int a, int b) {
		log4jlogger.debug("Inizio operazione divisione");
        double risultato = (double)a/(double)b;
        log4jlogger.info("Divisione eseguita: {} : {} = {}", a, b, risultato);
        return risultato;
	}
	public static void main(String[] args) {
		log4jlogger.info("Ciao non sto esplodendo");
	}
}

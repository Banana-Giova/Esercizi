package models;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class Calendario {
	private static Calendar calendar = Calendar.getInstance();
	private static String[] giorniSettimana = {"Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"};
	
	public static String CalendarCheck(int giorno, int mese, int anno) {
		String input_date = giorno + "/" + mese + "/" + anno;
		try {
            SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
            sdf.setLenient(false);
            Date user_date = sdf.parse(input_date);
			calendar.setTime(user_date);
			int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
			return giorniSettimana[dayOfWeek - 1];
		} catch (ParseException e) {
			System.out.println("Errore: La data inserita non è valida.\n" + e);
			return "ERROR";
		}
	}
}

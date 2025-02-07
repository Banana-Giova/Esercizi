package models;
import java.util.ArrayList;
import java.util.List;

public class IDChecker {
	protected static List<String> id_list = new ArrayList<String>();
	
	protected static boolean validateID(String new_id) {
		if (id_list.contains(new_id)) {
			return false;
		} else {
			id_list.add(new_id);
			return true;
		}
	}
}

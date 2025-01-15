package models;
import java.io.*;
import java.nio.file.*;

public class Contocorrente {
	
	private static double getSaldo() {
		BufferedReader reader = null;
		double output;
		File file = Paths.get("src", "db", "db.txt").toFile();
		
		try {
			reader = new BufferedReader(new FileReader(file));
			output = Double.parseDouble(reader.readLine());
		} catch (IOException e) {
			e.printStackTrace();
			output = 0.0;
		} finally {
			try {
				if (reader != null)
					reader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return output;
	}
	
	public static void setSaldo(double new_saldo) {
		BufferedWriter writer = null;
		File file = Paths.get("src", "db", "db.txt").toFile();
		
		try {
			writer = new BufferedWriter(new FileWriter(file));
			writer.write(new_saldo+"");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (writer != null)
					writer.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	protected static synchronized void prelievoSync(double somma) throws Exception {
		Thread.sleep(3000);
		 
		BufferedWriter bw = null;
		FileWriter fw = null;
		File file = Paths.get("src", "db", "db.txt").toFile();
		 
		try {
			double nuovoSaldo = getSaldo() - somma;
		 
			if(nuovoSaldo >= 0) {
					fw = new FileWriter(file);
					bw = new BufferedWriter(fw);
					bw.write(nuovoSaldo+"");
			} else {
				throw new Exception("Saldo insufficiente!");
			}
		} catch (IOException e) {
		e.printStackTrace();
		} finally {
			try {
				if (bw != null)
					bw.close();
				if (fw != null)
					fw.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	
	protected static void prelievoNonSync(double somma) throws Exception {
		Thread.sleep(3000);
		 
		BufferedWriter bw = null;
		FileWriter fw = null;
		File file = Paths.get("src", "db", "db.txt").toFile();
		 
		try {
			double nuovoSaldo = getSaldo() - somma;
		 
			if(nuovoSaldo >= 0) {
					fw = new FileWriter(file);
					bw = new BufferedWriter(fw);
					bw.write(nuovoSaldo+"");
			} else {
				throw new Exception("Saldo insufficiente!");
			}
		} catch (IOException e) {
		e.printStackTrace();
		} finally {
			try {
				if (bw != null)
					bw.close();
				if (fw != null)
					fw.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}

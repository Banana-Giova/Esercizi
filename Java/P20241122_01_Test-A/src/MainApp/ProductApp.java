package MainApp;
import models.*;
import java.util.*;

public class ProductApp {

	public static void main(String[] args) {
		ProductManager gestore_prodotti = new ProductManager();
		Elettronica op12r = new Elettronica("OnePlus 12R", 
										     550.0, 
										    "Telefono cellulare");
		Abbigliamento p_blauer = new Abbigliamento("Piumino Blauer",
													499.99,
												   "Abbigliamento invernale");
		Elettronica usb512 = new Elettronica("Pennetta USB 512GB Sandisk",
											  47.49,
											 "Dispositivo di archiviazione");
		Abbigliamento af1 = new Abbigliamento("Nike Air Force 1 bianche",
											   119.0,
											  "Scarpe da ginnastica");
		gestore_prodotti.addProd(op12r);
		gestore_prodotti.addProd(p_blauer);
		gestore_prodotti.addProd(usb512);
		gestore_prodotti.addProd(af1);
		ArrayList<Prodotto> list_prod = gestore_prodotti.getProdList();
		gestore_prodotti.viewProd();
		gestore_prodotti.sortByPrice(list_prod);
		System.out.println("\n\n↑\nPrima dell'ordinamento\n───────────────────\nDopo l'ordinamento\n↓\n\n");
		gestore_prodotti.viewProd();
	}
}

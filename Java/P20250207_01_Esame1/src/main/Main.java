package main;
import models.*;

public class Main {

    public static void main(String[] args) {
        Cliente cliente1 = new Cliente("Peppe", "Prosciutti", "dragopazzo@email.com", "password123", 200);
        cliente1.addToSaldo(1000);

        Cliente cliente2 = new Cliente("Lorenzo", "Faggi", "lorenzina@email.com", "password456", 300);
        cliente2.addToSaldo(500);
        
        Negozio negozio1 = new Negozio("Unieuro");
        Negozio negozio2 = new Negozio("Euronics");

        Smartphone smartphone1 = new Smartphone("iPhone 14", "Smartphone Apple", 999.99, "Apple", 4, 128, false);
        Smartphone smartphone2 = new Smartphone("OnePlus 12", "Smartphone OnePlus", 849.99, "OnePlus", 8, 256, false);
        Smartphone smartphone3 = new Smartphone("Google Pixel 6", "Smartphone Google", 599.99, "Google", 6, 128, true);

        Televisore televisore1 = new Televisore("LG OLED", "Televisore OLED 4K", 1799.99, "LG", 55, true);
        Televisore televisore2 = new Televisore("Samsung QLED", "Televisore QLED 4K", 1599.99, "Samsung", 65, true);
        Televisore televisore3 = new Televisore("Sony Bravia", "Televisore 4K LED", 1299.99, "Sony", 50, false);
        
        Computer computer1 = new Computer("MacBook Pro", "Laptop Apple con M1", 2399.99, "Apple", 16, 512, 13, true, true);
        Computer computer2 = new Computer("Dell XPS 13", "Laptop con Windows Pro", 1499.99, "Dell", 8, 256, 13, true, true);
        Computer computer3 = new Computer("HP Spectre x360", "Laptop 2-in-1", 1699.99, "HP", 16, 512, 13, true, false);
        System.out.println();
        negozio1.addProdotto(smartphone1);
        negozio1.addProdotto(televisore1);
        negozio1.addProdotto(computer1);
        
        negozio2.addProdotto(smartphone2);
        negozio2.addProdotto(smartphone3);
        negozio2.addProdotto(televisore2);
        negozio2.addProdotto(computer2);
        negozio2.addProdotto(computer3);
        negozio2.addProdotto(televisore3);
        System.out.println();
        negozio1.printProdotti();
        negozio2.printProdotti();
        System.out.println();
        cliente1.acquistaProdotto(negozio1, 1001);
        cliente2.acquistaProdotto(negozio2, 1002);
        cliente1.acquistaProdotto(negozio2, 1003);

        System.out.println("\nProdotti acquistati da " + cliente1.getNome() + " " + cliente1.getCognome() + ":");
        cliente1.printProdotti();

        System.out.println("\nProdotti acquistati da " + cliente2.getNome() + " " + cliente2.getCognome() + ":");
        cliente2.printProdotti();
    }
}

public class Studente extends Persona {
    private String corso;
    private int numeroMatricola;

    public Studente(String nome, int eta, String corso, int numeroMatricola) {
        super(nome, eta);
        this.corso = corso;
        this.numeroMatricola = numeroMatricola;
    }
    public String getCorso() {
        return corso;
    }
    public void setCorso(String corso) {
        this.corso = corso;
    }
    public int getNumeroMatricola() {
        return numeroMatricola;
    }
    public void numeroMatricola(int numeroMatricola) {
        this.numeroMatricola = numeroMatricola;
    }

    public String toString() {
        return super.toString() +",corso = " + corso + ", numeroMatricola = " + numeroMatricola + ".";
    }


}
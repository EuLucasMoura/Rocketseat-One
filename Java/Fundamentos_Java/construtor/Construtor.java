package construtor;

public class Construtor {
    
    private int numero;

    public Construtor(int numero, String texto) {
        System.out.println("Construtor com um parâmetro criado.");
        this.numero = numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getNumero() {
        return numero;
    }
}

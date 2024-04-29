package primeirasAulas;
import java.util.ArrayList;
import java.util.List;

public class EstruturaDeDados {
    /**
     * @param args
     */
    public static void main(String[] args) {
        // lista
        List<String> nomes = new ArrayList<>();
        nomes.add("Lucas");
        nomes.add("Victoria");
        nomes.add("Pedro");

        //System.out.println(nomes.get(0));

        // for (String nome : nomes) {
        //     System.out.println("O nome é " + nome);
        // }

        nomes.forEach(nome -> System.out.println("O nome que apareceu foi: " + nome));
    }
}

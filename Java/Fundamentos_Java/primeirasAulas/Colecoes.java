package primeirasAulas;
import java.util.HashMap;
import java.util.Map;

public class Colecoes {
    public static void main(String[] args) {
        Map<String, Integer> notas = new HashMap<>();
        notas.put("Lucas", 10);
        notas.put("Victoria", 9);
        notas.put("Pedro", 9);

        for (Map.Entry<String, Integer> entry : notas.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();

            System.out.println("A chave é " +  key + " e o valor é " + value);
        }
    }
}

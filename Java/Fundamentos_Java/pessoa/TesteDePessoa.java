package pessoa;

public class TesteDePessoa {
    
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        pessoa.cpf = "333.222.888-66";
        pessoa.nome = "Lucas";
        pessoa.idade= 23;

        System.out.println(pessoa.imprimirDadosDaPessoa());
    }
}

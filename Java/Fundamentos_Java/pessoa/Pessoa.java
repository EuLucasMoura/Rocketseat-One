package pessoa;

public class Pessoa {
   
    String nome;
    int idade;
    String cpf;

    String imprimirDadosDaPessoa() {
        return "O nome da pessoa é " + nome + " a idade é " + idade + " e o cpf é " + cpf;
    }

}

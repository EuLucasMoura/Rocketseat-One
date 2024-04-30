package pessoa;

public class TesteDePessoa {
    
    public static void main(String[] args) {
        Professor professor = new Professor();
        professor.setCpf("333.222.888-66");
        professor.setNome("Lucas");
        professor.setIdade(23);
        professor.setSalario(5000);

        Aluno aluno = new Aluno();
        aluno.setCpf("123.456.789-99");
        aluno.setNome("Victoria");
        aluno.setIdade(16);
        aluno.setMatricula("1");

        Pessoa pessoa3 = new Pessoa();
        pessoa3.setCpf("987.654.321-11");
        pessoa3.setNome("Pedro");
        pessoa3.setIdade(18);


        System.out.println(professor.imprimirDadosDaPessoa());

        System.out.println(aluno.imprimirDadosDaPessoa());
    }
}

/*
 * HelloWorld = Nome da minha classe
 * public = Tipo de acesso da minha classe
 * class = tipo da classe 
 */


public class  HelloWorld {
    
    //todo conteudo devera ser inserido aqui dentro 

    public static void main(String[] args) {
        /*
         * Valores (int. double, float, long)
         * Textp (String)
         * Booleanos (boolean)
         */

         int dadoDoTipoint = 10;
         double dadoDoTipoDouble = 3.14;
         float dadoDoTipoFloat = 3.14f;
         long dadoDoTipoLong= 893218491284912L;
         String dadoDoTipoString = "Colocar o meu Texto";
         boolean dadoTipoBoolean = false;

        if (dadoDoTipoint == 10) {
            //sysout
            System.out.println("Entrou no if do 10");
        }
        if (dadoDoTipoint < 12) {
            System.out.println("Entrou no if do 12");
        }

        else {
            System.out.println("Entrou no else");
        }

        // While  (Enquanto algo for verdadeiro faça alguma coisa)
        int valorInicial = 0;  
        while (valorInicial < 10) {
            System.out.println("O valor e menor do que 3");
            System.out.println(valorInicial);
            valorInicial ++; // contador somando mais um on valorInicial
        }

        //for 
        for( int i = 0; i < 4 ; i++) {
            System.out.println("O valor do i e: " + i);
        }

    }
}

//fora do escopo da classe
import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Cria um vetor de Strings com tamanho 10
        String[] fabricante = new String[10];
        Scanner scanner = new Scanner(System.in);

        // Loop para preencher o vetor com nomes de cidades
        for (int i = 0; i < fabricante.length; i++) {
            System.out.print("Insira o nome da cidade " + (i + 1) + ": ");
            fabricante[i] = scanner.nextLine();
        }

        // Copia o vetor para outra variável (referência ao mesmo array)
        String[] cidades = fabricante;

        // Exibe todas as cidades cadastradas
        System.out.println("Cidades cadastradas:");
        System.out.println(Arrays.toString(cidades));
    }
}

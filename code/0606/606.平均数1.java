import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble(), b = sc.nextDouble();
        System.out.printf("MEDIA = %.5f", ((3.5 * a + 7.5 * b) / (3.5 + 7.5)));
    }
}

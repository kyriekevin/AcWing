import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        double h = sc.nextDouble(), s = sc.nextDouble();
        System.out.printf("NUMBER = %d\n", x);
        System.out.printf("SALARY = U$ %.2f", h * s);
    }
}


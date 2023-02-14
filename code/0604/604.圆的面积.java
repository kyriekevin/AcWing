import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final double pi = 3.14159;
        double r = sc.nextDouble();
        System.out.printf("A=%.4f", pi * r * r);
    }
}

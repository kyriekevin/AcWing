import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        final int[] a = {100, 50, 20, 10, 5, 2, 1};
        System.out.println(n);

        for (int i = 0; i < 7; ++i) {
            int cnt = n / a[i];
            System.out.printf("%d nota(s) de R$ %d,00\n", n / a[i], a[i]);
            n %= a[i];
        }
    }
}

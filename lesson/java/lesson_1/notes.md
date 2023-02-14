# 1. A + B
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt(), y = sc.nextInt();
        System.out.println(x + y);
    }
}
```

# 608. 差
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        int c = sc.nextInt(), d = sc.nextInt();
        System.out.printf("DIFERENCA = %d", (a * b - c * d));
    }
}
```

# 604. 圆的面积
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final double pi = 3.14159;
        double r = sc.nextDouble();
        System.out.printf("A=%.4f", pi * r * r);
    }
}
```

# 606. 平均数1
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble(), b = sc.nextDouble();
        System.out.printf("MEDIA = %.5f", ((3.5 * a + 7.5 * b) / (3.5 + 7.5)));
    }
}
```

# 609. 工资
```java
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
```

# 615. 油耗
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x = sc.nextDouble(), y = sc.nextDouble();
        System.out.printf("%.3f km/l", x / y);
    }
}
```

# 616. 两点间的距离
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x1 = sc.nextDouble(), y1 = sc.nextDouble();
        double x2 = sc.nextDouble(), y2 = sc.nextDouble();
        double dx = x1 - x2, dy = y1 - y2;
        System.out.printf("%.4f", Math.sqrt(dx * dx + dy * dy));
    }
}
```

# 653. 钞票
```java
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
```

# 654. 时间转换
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int hours = n / 3600;
        n %= 3600;
        int minutes = n / 60;
        int seconds = n % 60;

        System.out.printf("%d:%d:%d\n", hours, minutes, seconds);
    }
}
```

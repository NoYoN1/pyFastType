import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        // int a = 7;
        // if (a > 3) {
        // System.out.println("3");
        // if (a < 5) {
        // System.out.println("5");
        // if (a == 7) {
        // System.out.println("7");
        // }
        // }
        // }
        Scanner sc = new Scanner(System.in);
        System.out.print("insert number: ");
        // int input = sc.nextInt();
        int input = 15;
        for (int i = 1; i <= input; i++) {
            System.out.print("\n" + i);
            if (i % 3 == 0) {
                System.out.print(" print 3");
            }
            if (i % 5 == 0) {
                System.out.print(" print 5");
            }
        }
        sc.close();
    }
}

// import java.util.*;

// public class Test {
// public static void main(String[] args) {
// int n = 0;
// String str1 = "Fizz";
// String str2 = "Buzz";

// do {
// n++;
// System.out.print("\n" + n + ". ");

// if (n % 3 == 0) {
// System.out.print(str1);
// }
// if (n % 5 == 0) {
// System.out.print(str2);
// }
// } while (n % 3 != 0 || n % 5 != 0);
// System.out.println(" ");
// }
// }
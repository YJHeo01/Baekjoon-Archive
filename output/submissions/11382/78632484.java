import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String strA = scanner.next();
        String strB = scanner.next();
        String strC = scanner.next();
        long a = Long.parseLong(strA);
        long b = Long.parseLong(strB);
        long c = Long.parseLong(strC);
        long answer = a+b+c;
        System.out.println(answer);
    }
}
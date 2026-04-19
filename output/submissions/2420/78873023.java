import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextInt();
        long b = scanner.nextInt();
        long answer = a-b;
        answer = Math.abs(answer);
        System.out.println(answer);
        scanner.close();
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = "CWelcomeToSMUP";
        int n = scanner.nextInt();
        n %= 14;
        System.out.println(str.substring(n,n+1));
    }
}
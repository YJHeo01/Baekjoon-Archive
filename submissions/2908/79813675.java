import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str1 = scanner.next();
        String str2 = scanner.next();
        
        String tmp1 = String.valueOf(str1.charAt(2)) + String.valueOf(str1.charAt(1)) + String.valueOf(str1.charAt(0));
        String tmp2 = String.valueOf(str2.charAt(2)) + String.valueOf(str2.charAt(1)) + String.valueOf(str2.charAt(0));

        int num1 = Integer.parseInt(tmp1);
        int num2 = Integer.parseInt(tmp2);

        int answer = num1 > num2 ? num1 : num2;
        System.out.println(answer);
    }
}
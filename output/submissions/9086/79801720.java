import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i=0;i<n;i++){
            String str = scanner.nextLine();
            int length = str.length();
            char left = str.charAt(0);
            char right = str.charAt(length-1);
            System.out.println(left+""+right);
        }
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int answer = pibonachi(n);
        System.out.println(answer);
    }
    public static int pibonachi(int n){
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        return pibonachi(n-1)+pibonachi(n-2);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int answer = 0;
        int value = 0;
        int idx = 0;
        while (true) {
            value += 1;
            if(value>n){
                break;
            }
            if(n%value == 0){
                idx += 1;
                if(idx==k){
                    answer = idx;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
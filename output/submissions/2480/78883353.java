import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int answer = 0;
        if(a==b){
            answer = 1000 + a * 100;
            if(b==c){
                answer *= 10;
            }
        }else{
            if(b==c){
                answer = 1000 + b * 100;
            }else{
            answer = a;
            if(b > answer) answer = b;
            if(c > answer) answer = c;
            answer *= 100;
            }
        }
        System.out.println(answer);
    }
}
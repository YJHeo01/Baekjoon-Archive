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
                if(a>b){
                    if(a>c){
                        answer = a * 100;
                    }else{
                        answer = c * 100;
                    }
                }else{
                    if(b>c){
                        answer = b * 100;
                    }else{
                        answer = c * 100;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
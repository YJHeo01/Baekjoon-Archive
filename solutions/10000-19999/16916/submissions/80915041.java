import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.next();
        String P = scanner.next();
        int answer = 0;
        for(int i=0;i<S.length()-P.length();i++){
            if(P.equals(S.substring(i, i+P.length()))){
                answer = 1;
                break;
            }
        }
        if(P.equals(S)) answer = 1;
        System.out.println(answer);
    }
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.next();
        String P = scanner.next();
        int answer = 0;
        int Plength = P.length();
        int Slength = S.length() - Plength;
        for(int i=0;i<Slength;i++){
            if(P.equals(S.substring(i, i+Plength))){
                answer = 1;
                break;
            }
        }
        if(P.equals(S)) answer = 1;
        System.out.println(answer);
    }
}
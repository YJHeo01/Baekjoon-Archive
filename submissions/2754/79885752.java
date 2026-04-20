import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String grade = scanner.next();
        if(grade.equals("F")){
            System.out.println("0.0");
            return;
        }
        double answer = 0;
        String alphabet = grade.substring(0,1);
        String plus_minus = grade.substring(1);
        if(alphabet.equals("A")){
            answer += 4;
        }else if(alphabet.equals("B")){
            answer += 3;
        }else if(alphabet.equals("C")){
            answer += 2;
        }else{
            answer += 1;
        }

        if(plus_minus.equals("+")){
            answer += 0.3;
        }

        if(plus_minus.equals("-")){
            answer -= 0.3;
        }
        System.out.println(answer);
    }
}
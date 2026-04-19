import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();
        int answer = 0;
        for(int i=0;i<str.length();i++){
            switch (str.charAt(i)) {
                case 'A', 'B', 'C':
                    answer += 3;
                    break;
                case 'D', 'E', 'F':
                    answer += 4;
                    break;
                case 'G', 'H', 'I':
                    answer += 5;
                    break;
                case 'J', 'K', 'L':
                    answer += 6;
                    break;
                case 'M', 'N', 'O':
                    answer += 7;
                    break;
                case 'P', 'Q', 'R', 'S':
                    answer += 8;
                    break;
                case 'T', 'U', 'V':
                    answer += 9;
                    break;
                default:
                    answer += 10;
                    break;
            }
        }
        System.out.println(answer);
    }
}
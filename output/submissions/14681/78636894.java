import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str_X = scanner.nextLine();
        int x = Integer.parseInt(str_X);
        String Str_Y = scanner.nextLine();
        int y = Integer.parseInt(Str_Y);
        int answer = 0;
        if(x < 0){
            if(y < 0)answer = 3;
            else answer = 2;
        }else{
            if(y < 0)answer = 4;
            else answer = 1;
        }
        System.out.println(answer);
    }
}
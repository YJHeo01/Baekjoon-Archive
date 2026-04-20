import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean[] homework = new boolean[31];
        for(int i=0;i<28;i++){
            int n = scanner.nextInt();
            homework[n] = true;
        }
        for(int i=1;i<=30;i++){
            if(homework[i]==false){
                System.out.println(i);
            }
        }
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] array = new int[100];
        for(int i=0;i<n;i++){
            int tmp = scanner.nextInt();
            array[i] = tmp;
        }
        int answer = 0;
        int v = scanner.nextInt();
        for(int i=0;i<n;i++){
            if(v==array[i]){
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}
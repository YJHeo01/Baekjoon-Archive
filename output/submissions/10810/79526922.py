import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[] array = new int[n+1];
        for(int x=0;x<m;x++){
            int i = scanner.nextInt();
            int j = scanner.nextInt();
            int k = scanner.nextInt();
            for(int y=i;y<=j;y++){
                array[y] = k;
            }
        }
        for(int i=1;i<=n;i++){
            System.out.print(array[i] + " ");
        }
    }
}
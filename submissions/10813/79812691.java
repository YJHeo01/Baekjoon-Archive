import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[] _array = new int[n+1];
        for(int i=1;i<=n;i++){
            _array[i] = i;
        }
        for(int t=0;t<m;t++){
            int i = scanner.nextInt();
            int j = scanner.nextInt();
            int tmp = _array[i];
            _array[i] = _array[j];
            _array[j] = tmp;
        }
        for(int i = 1; i <= n; i++){
            System.out.print(_array[i] + " ");
        }
    }
}
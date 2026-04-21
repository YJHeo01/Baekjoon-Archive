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
        for(int x=0;x<m;x++){
            int i = scanner.nextInt();
            int j = scanner.nextInt();
            int mid = j / 2;
            for(int k=0;k<=mid;k++){
                int tmp = _array[i+k];
                _array[i+k] = _array[j-k];
                _array[j-k] = tmp;
            }
        }
        for(int i=1;i<=n;i++){
            System.out.print(_array[i]+" ");
        }
    }
}
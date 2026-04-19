import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        boolean[] not_prime = new boolean[n+1];
        not_prime[1] = true;
        for(int i=2;i<=n;i++){
            if(not_prime[i]==false){
                for(int j=i*2;j<=n;j+=i){
                    not_prime[j] = true;
                }
            }
        }
        int min_prime = -1;
        int sum_prime = 0;
        for(int i=m;i<=n;i++){
            if(not_prime[i]==false){
                sum_prime += i;
                if(min_prime==-1){
                    min_prime = i;
                }
            }
        }
        if(sum_prime!=0){
            System.out.println(sum_prime);
        }
        System.out.println(min_prime);
    }
}
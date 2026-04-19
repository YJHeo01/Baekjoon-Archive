import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] friends = new String[n];
        for(int i=0;i<n;i++){
            friends[i] = scanner.next();
        }
        String me = scanner.next();
        int answer = 0;
        for(String i:friends){
            if(me.equals(i)){
                answer++;
            }
        }
        System.out.println(answer);
    }
}
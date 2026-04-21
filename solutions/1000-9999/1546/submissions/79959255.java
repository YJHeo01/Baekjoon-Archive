import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        double[] score = new double[n];
        double max_value = 0;
        for(int i=0;i<n;i++){
            score[i] = scanner.nextDouble();
            if(score[i]>max_value){
                max_value = score[i];
            }
        }
        double answer = 0;
        for(int i=0;i<n;i++){
            answer += score[i]/max_value*100;
        }
        answer /= n;
        System.out.println(answer);
    }
}
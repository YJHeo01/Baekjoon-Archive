import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            if(a==0 && b == 0 && c == 0){
                return;
            }
            int[] array = {a,b,c};
            for(int i=2;i>=0;i--){
                for(int j=0;j<i;j++){
                    if(array[j]>array[j+1]){
                        int bigger_value = array[j];
                        array[j] = array[j+1];
                        array[j+1] = bigger_value;
                    }
                }
            }
            if(array[2] >= array[1] + array[0]){
                System.out.println("Invalid");
                continue;
            }
            int state = 0;
            String[] answer = {"Scalene","Isosceles","Equilateral"};
            for(int i=0;i<2;i++){
                if(array[i] == array[i+1]){
                    state++;
                }
            }
            System.out.println(answer[state]);
        }

    }
}
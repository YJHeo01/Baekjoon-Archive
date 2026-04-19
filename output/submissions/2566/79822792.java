import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max_value = -1;
        int max_value_row = 0;
        int max_value_column = 0;
        for(int r=1;r<=9;r++){
            for(int c=1;c<=9;c++){
                int tmp = scanner.nextInt();
                if(tmp>max_value){
                    max_value = tmp;
                    max_value_row = r;
                    max_value_column = c;
                }
            }
        }
        System.out.println(max_value);
        System.out.println(max_value_row + " " + max_value_column);
    }
}
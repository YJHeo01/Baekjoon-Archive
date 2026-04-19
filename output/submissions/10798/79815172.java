import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] array = new String[5];
        int[] length = new int[5];
        for(int i=0;i<5;i++){
            array[i] = scanner.next();
            length[i] = array[i].length();
        }
        for(int i=0;i<15;i++){
            for(int j=0;j<5;j++){
                if(i>=length[j]){
                    continue;
                }
                System.out.print(array[j].charAt(i));
            }
        }
    }
}
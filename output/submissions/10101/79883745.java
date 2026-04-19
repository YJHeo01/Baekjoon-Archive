import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] _array = new int[3];
        for(int i=0;i<3;i++){
            _array[i] = scanner.nextInt();
        }
        String[] answer = {"Scalene","Isosceles","Error","Equilateral"};
        int state = 0;
        for(int i=0;i<3;i++){
            if(_array[i]==_array[(i+1)%3]){
                state++;
            }
        }
        if(_array[0]+_array[1]+_array[2] != 180){
            state = 2;
        }
        System.out.println(answer[state]);
    }
}
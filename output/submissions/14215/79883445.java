import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] _array = new int[3];
        for(int i=0;i<3;i++){
            _array[i] = scanner.nextInt();
        }
        for(int i=1;i<3;i++){
            for(int j=0;j<i;j++){
                if(_array[j]>_array[j+1]){
                    int bigger_value = _array[j];
                    _array[j] = _array[j+1];
                    _array[j+1] = bigger_value;
                }
            }
        }
        int biggest_value = _array[2];
        int others_value = _array[0] + _array[1];
        while (true) {
            if(others_value>biggest_value){
                break;
            }
            biggest_value--;
        }
        int answer = biggest_value + others_value;
        System.out.println(answer);

    }
}
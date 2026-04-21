import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] _array = new String[3];
        for(int i=0;i<3;i++){
            _array[i] = scanner.next();
        }
        int value = 0;
        for(int i=2;i>=0;i--){
            if(_array[i].equals("Fizz") || _array[i].equals("Buzz") || _array[i].equals("FizzBuzz") ){
                continue;
            }
            value = Integer.parseInt(_array[i]) + 3 - i;
            break;
        }
        if(value % 3 != 0 && value % 5 != 0){
            System.out.println(value);
        }else if(value % 3 == 0){
            System.out.println("Fizz");
        }else if(value % 5 == 0){
            System.out.println("Buzz");
        }else{
            System.out.println("FizzBuzz");
        }
    }
}
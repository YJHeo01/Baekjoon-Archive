import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hour = scanner.nextInt();
        int minute = scanner.nextInt();
        int c = scanner.nextInt();
        if(minute+c < 60){
            minute += c;
        }else{
            int plus_hour = c / 60;
            int plus_minute = c % 60;
            hour += plus_hour;
            minute += plus_minute;
            if(minute >= 60){
                minute -= 60;
                hour += 1;
            }
            hour %= 24;
        }
        System.out.println(hour + " " + minute);
    }
}
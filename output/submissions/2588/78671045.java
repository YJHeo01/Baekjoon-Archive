import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        int third = first * (second%10);
        int fourth = (first * (second%100) - third)/10;
        int fifth = (first * second - third - fourth*10)/100;
        int sixth = first * second;
        System.out.println(third);
        System.out.println(fourth);
        System.out.println(fifth);
        System.out.println(sixth);
        scanner.close();
    }
}
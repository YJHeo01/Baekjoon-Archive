public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int answer = Math.abs(a-b);
        System.out.println(answer);
        scanner.close();
    }
}
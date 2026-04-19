import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean HE_GOT_AWAY = true;
        for(int i=1;i<=5;i++){
            String s = scanner.next();
            for(int j=3;j<=s.length();j++){
                if(s.substring(j-3, j).equals("FBI")){
                    HE_GOT_AWAY = false;
                    System.out.print(i + " ");
                    break;
                }
            }
        }
        if(HE_GOT_AWAY==true){
            System.out.println("HE GOT AWAY!");
        }
    }
}
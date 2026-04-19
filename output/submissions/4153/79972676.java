import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int[] edges = new int[3];

            for(int i=0;i<3;i++){
                edges[i] = scanner.nextInt();
            }

            boolean finish = true;
            for(int i=0;i<3;i++){
                if(edges[i]!=0){
                    finish = false;
                    break;
                }
            }

            if(finish == true) break;

            for(int i=2;i>=0;i--){
                for(int j=0;j<i;j++){
                    if(edges[j+1] > edges[j]){
                        int tmp = edges[j];
                        edges[j] = edges[j+1];
                        edges[j+1] = tmp;
                    }
                }
            }

            if(edges[0] * edges[0] == edges[1] * edges[1] + edges[2] * edges[2]){
                System.out.println("right");
            }else{
                System.out.println("wrong");
            }
        }
    }
}
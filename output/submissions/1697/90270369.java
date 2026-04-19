// 타인 코드 피드백 중 시간복잡도 체크를 위한 제출
import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in); // 1
        int n=s.nextInt(),k=s.nextInt(),r=0,M=100001; // 1
        boolean[] T=new boolean[M]; // 1
        Queue<Integer> q=new LinkedList<>(); // 1
        q.offer(n); // 1
        L:do{
            int z=q.size(), i=0; // 얘들은 몇번 실행하지..? 근데 안의 do문보단 적을 것같은데..
            do {
                i++;
                int x=q.poll(); // 정점의 개수, 방문 여부를 관리하는 
                if(x==k) break L; // 1
                else if(((x<0)||(x>=M))||(T[x]==true)) continue; // 1이상..?
                else {
                    T[x]=true; // 여기도 else로 묶여있지만 결국 여기도 O(N)..?
                    q.offer(x*2); //
                    q.offer(x-1); //
                    q.offer(x+1); //
                }
            } while (i<z);
            r++; //얘도 O(N) 아닐까 싶음
        }while(!(q.isEmpty()));
        System.out.print(r); //1
    }
} //그럼 최종은 O(N)? 인가? 그게 되나..?
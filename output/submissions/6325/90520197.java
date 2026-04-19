import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader I=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter O=new BufferedWriter(new OutputStreamWriter(System.out));

        int t,n=0; //반복 변수
        while((t=Integer.parseInt(I.readLine()))!=0){
            StringBuilder ca=new StringBuilder("a"); n++; // 값을 가진 변수는 현재 a하나 뿐, n은 반복문의 카운트 
            Set<Character> S=new HashSet<>();
            S.add('a');
            while(t-->0){
                String v=I.readLine();
                char v1=v.charAt(0),v2=v.charAt(4);
                //System.out.println("v1: "+v1+" v2: "+v2);
                if(S.contains(v2)){
                    ca.append(v1);
                    S.add(v1);
                    //System.out.println("추가할 v1: "+v1+"\n");
                    continue;
                }
                S.remove(v1);
            }
            //System.out.println(ca);
            O.write("Program #"+n+"\n");
            for(char c:S){
                O.write(c+" ");
            }
            if(S.isEmpty()) O.write("none\n"); continue;
            O.write("\n\n");
            
        }
        O.flush();
    }
}
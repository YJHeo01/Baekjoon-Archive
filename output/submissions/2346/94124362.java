import java.io.*;
import java.util.*;
class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader I=new BufferedReader(new InputStreamReader(System.in));

        StringBuilder as=new StringBuilder();
        int n=Integer.parseInt(I.readLine());
        int[] bal=new int[n],op=new int[n];

        StringTokenizer st=new StringTokenizer(I.readLine());
        for(int i=0;i<n;i++){
            bal[i]=Integer.parseInt(st.nextToken());
        }

        int ct=n,id=0;

        for(int i=0;i<n;i++){
            op[i]=id+1;
            int mv=bal[id];
            bal[id]=0;
            while(mv>0){
                if(++id==n) id=0; 
                if(bal[id]!=0) mv--;
            }
            while(mv<0){
                if(--id<0) id=n-1;
                if(bal[id]!=0) mv++;
            }
        }

        for(int i:op){
            as.append(i).append(' ');
        }

        System.out.println(as);
    }
}
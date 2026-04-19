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

        int ct=0,id=0;

        for(int j=0;j<n;j++){
            op[ct++]=id+1;
            int mv=bal[id];
            bal[id]=0;
            if(mv>0){
                int t=0;
                for(int i=0;i<mv;){
                    if(bal[id++]!=0){
                        i++;
                    }
                    if(id==n) id=0;
                    if(++t==n*n+1) break;
                }
                id--;
                if(id<0) id=n-1;
            }else{
                int t=0;
                for(int i=mv;i<0;){
                    if(bal[id--]!=0){
                        i++;
                    }
                    if(id<0) id=n-1;
                    if(++t==n*n+1) break;
                }
                id++;
                if(id==n) id=0;
            }
        }
        
        for(int i:op){
            as.append(i).append(' ');
        }

        System.out.println(as);
    }
}
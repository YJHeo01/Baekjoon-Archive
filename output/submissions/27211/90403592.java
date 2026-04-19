import java.io.*;
import java.util.*;
class Main{
    static int n,m,sn,sm;
    static int[][] donut; 
    static Deque<Integer> q=new ArrayDeque<>();
    static int[] ax={-1,1,0,0},ay={0,0,-1,1};
    public static void bfs(){
        while(!q.isEmpty()){
            int x=q.poll(),y=q.poll();
            donut[x][y]=1;
            for(int i=0;i<4;i++){
                int tx=x+ax[i],ty=y+ay[i];
                if(tx<0) tx+=n; else if(tx>sn)tx-=n;
                if(ty<0) ty+=m; else if(ty>sm)ty-=m;
                if(donut[tx][ty]==0){
                    donut[tx][ty]=1
                    q.offer(tx);
                    q.offer(ty);
                }
            }
        }
    }
    public static void main(String[] args)throws Exception{
        BufferedReader I=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter O=new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer s=new StringTokenizer(I.readLine());
        n=Integer.parseInt(s.nextToken()); m=Integer.parseInt(s.nextToken());
        sn=n-1; sm=m-1;
        donut=new int[n][m];
        for(int i=0;i<n;i++){
            s=new StringTokenizer(I.readLine());
            for(int j=0;j<m;j++){
                donut[i][j]=Integer.parseInt(s.nextToken());
            }
        }
        int a=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(donut[i][j]==0){
                    q.offer(i); q.offer(j);
                    bfs();
                    a++;
                }
            }
        }
        O.write(a+"\n");
        O.flush();
    }
}
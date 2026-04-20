#include <stdio.h>

int main(){
    int n,k,biggest;
    int x[1000];
    scanf("%d %d",&n,&k);
    for(int i=0;i<n;i++){
        scanf("%d",&x[i]);
    }

    for(int i=0;i<n-1;i++){
        biggest = i;
        for(int j=i+1;j<n;j++){
            if(x[biggest]<x[j]){
                biggest = j;
            }
        }
        int tmp = x[biggest];
        x[biggest] = x[i];
        x[i] = tmp;
    }
    printf("%d",x[k-1]);
}
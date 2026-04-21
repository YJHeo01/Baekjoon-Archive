#include <stdio.h>

int main(){
    int sum_value = 0;
    int min_value = 100;
    for(int i=0;i<7;i++){
        int tmp;
        scanf("%d",&tmp);
        if(tmp%2==0) continue;
        sum_value+=tmp;
        if(min_value>tmp){
            min_value = tmp;
        }
    }
    if(sum_value==0) printf("-1");
    else{
        printf("%d\n",sum_value);
        printf("%d",min_value);
    }
}
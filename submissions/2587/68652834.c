#include <stdio.h>

int main(){
    int sum = 0;
    int num[5] = {0};
    for(int i=0;i<5;i++){
        scanf("%d",&num[i]);
        sum += num[i];
    }
    int tmp;
    for(int i=5;i>0;i--){
        for(int j=0;j<i-1;j++){
            if(num[j]>num[j+1]){
                tmp = num[j];
                num[j] = num[j+1];
                num[j+1] = tmp;
            }
        }
    }
    printf("%d\n",sum/5);
    printf("%d",num[2]);
}
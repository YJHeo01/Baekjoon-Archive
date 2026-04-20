#include <stdio.h>
#include <string.h>
int main(){
    char arr[1000000] ={0,};
    scanf("%s",arr);
    int length = strlen(arr);
    for(int i=0;i<length;i++){
        if(i%10==0&&i!=0)printf("\n");
        printf("%c",arr[i]);
    }
    return 0;
}
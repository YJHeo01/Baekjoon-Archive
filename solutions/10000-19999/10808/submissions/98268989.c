#include <stdio.h>
#include <string.h>

int main(){
    char arr[1000000] ={0,};
    scanf("%s",arr);
    int length = strlen(arr);
    int answer[26]={0,};
    for(int i=0;i<length;i++){
        answer[arr[i]-'a']++;
    }
    for(int i=0;i<26;i++){
        printf("%d ",answer[i]);
    }
}
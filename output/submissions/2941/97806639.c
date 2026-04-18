#include <stdio.h>
int main(){
    char arr[100];
    int i;
    int count=0;
    
    scanf("%s",arr);
    int len = strlen(arr);
    
    for(i=0; i<strlen(arr); i++){
        if(arr[i]=='c')
            if(arr[i+1]=='='|| arr[i+1]=='-')
            {--len; continue;}  
        if(arr[i]=='d')
            if(arr[i+1]=='z')
            	if(arr[i+2]=='=')
            	{len--; continue;}
         if(arr[i]=='d')
            if(arr[i+1]=='-')
            	{--len; continue;}
        
        if(arr[i]=='l' || arr[i]=='n')
        	if(arr[i+1]=='j')
               {--len; continue;}
        if(arr[i]=='s' || arr[i]=='z')
        	if(arr[i+1]=='=')
        	   {--len; continue;}
    }
    
    printf("%d",len);
    
    return 0;
}
#include <stdio.h>

int heap[100000] = {0};
int last_i = 0;

void swap(int a, int b){
    int tmp = heap[a];
    heap[a] = heap[b];
    heap[b] = tmp;
}

int pop_heap(void){
    if(last_i==0){
        return 0;
    }
    int ret_value = heap[1];
    heap[1] = heap[last_i--];
    int cur_i = 1;
    while(1)
    {
        int biggest = cur_i;
        int left = cur_i * 2;
        int right = left + 1;
        if(heap[cur_i]<heap[left] && left <= last_i){
            biggest = left;
        }else if(heap[cur_i]<heap[right] && right <= last_i){
            biggest = right;
        }else{
            return ret_value;
        }
        swap(biggest,cur_i);
        cur_i = biggest;    
    }
}

void push_heap(int x){
    heap[++last_i] = x;
    int cur_i = last_i;
    int parent_i = cur_i / 2;
    while(parent_i>=1){
        if(heap[parent_i]>=heap[cur_i]){
            return;
        }else{
            swap(parent_i,cur_i);
            cur_i = parent_i;
            parent_i = cur_i/2;
        }
    }
}
int main(){

    int n,x;
    int value = 0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&x);
        switch(x){
            case 0:
                value = pop_heap();
                printf("%d\n",value);
                break;
            default:
                push_heap(x);
        }
    }
}
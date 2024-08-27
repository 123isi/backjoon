#include <stdio.h>
int main(void) {
    int x;
    scanf("%d",&x);
    int li[10001]={};
    for(int i=0;i<x;i++){
        int temp;
        scanf("%d",&temp);
        li[temp]++;
    }
   
    
    for(int i=0;i<10001;i++){
        for(int j=0;j<li[i];j++){
            printf("%d\n",i);
            }
    }
}

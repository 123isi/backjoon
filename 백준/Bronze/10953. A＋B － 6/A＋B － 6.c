#include <stdio.h>
int main(void){
    char a;
    int x;
    int c,d;
    scanf("%d",&x);
    for(int i=0;i<x;i++){
        scanf("%d%c%d",&c,&a,&d);
        printf("%d\n",c+d);
    }
    return 0;
}


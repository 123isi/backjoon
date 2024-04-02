#include <stdio.h>
int main(void){
    int x,a;
    scanf("%d",&x);
    a=1;
    if(x!=0){
        for(;x!=0;x--){
            a*=x;
        }
        printf("%d",a);
    }
    else{
        printf("%d",1);
    }
    return 0;
}

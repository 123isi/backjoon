#include <stdio.h>
int main(void){
    int x;
    long long int a=1;
    scanf("%d",&x);
    for(int i=1;i<=x;i++)
    {
        a=a*i;
    }
    if(x!=0){
        printf("%lld",a);
    }
    else{
        printf("%d",1);
    }
    return 0;
}

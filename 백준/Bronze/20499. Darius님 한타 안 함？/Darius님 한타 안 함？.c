#include <stdio.h>
int main(void){
    
    int x,y,z;
    char a;
    scanf("%d %c %d %c %d",&x,&a,&y,&a,&z);
    if(y==0 || x+z<y) {
        printf("hasu");
    }
    else{
        printf("gosu");
    }
}



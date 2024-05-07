#include <stdio.h>
#include <string.h>
int main(void){
    int x;
    int y;
    char a[1002];
    scanf("%d",&x);
    for(int i=0;i<x;i++){
        scanf("%d %s",&y,a);
        for(int j=0;j<strlen(a);j++){
            for(int k=0;k<y;k++){
                printf("%c",a[j]);
            }
        }
        printf("\n");
    }
    return 0;
}

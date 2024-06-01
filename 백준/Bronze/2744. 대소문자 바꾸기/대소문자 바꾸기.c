#include <stdio.h>
int main(void){
    char arr[101];
    int a = 0;
    int x;
    scanf("%s", arr);
    while(1){
        x = arr[a];
        if (x == '\0') break;
        if(x >= 97) printf("%c", x - 32);
        else printf("%c", x + 32);

        ++a;
    }
    return 0;
}

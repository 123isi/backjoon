#include <stdio.h>
#include <stdlib.h>
int main(void) {
    char *str = (char*)malloc(sizeof(char)*7);
    scanf("%s",str);
    int arr[9]={};
    for(int i=0;str[i]!='\0';i++) {
        if(str[i]-'0'==9) arr[6]++;
        else arr[str[i]-'0']++;
    }
    arr[6] = (arr[6]+1)/2;
    int max=0;
    for(int i=0;i<9;i++) {
        if(max<arr[i]) max=arr[i];
    }
    printf("%d",max);
}
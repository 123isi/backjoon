#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    double d = a*(b*0.01);
    printf(a-d>=100?"0":"1");

    return 0;
}
#include <stdio.h>

int main()
{
    int a, b, c;
    int a1, b1, c1;

    while (1)
    {
        scanf("%d %d %d",&a ,&b ,&c);
        if(a == 0 && b == 0 && c == 0)
        break;
        a1 = a * a;
        b1 = b * b;
        c1 = c * c;
        if(a1 == b1 + c1 || b1 == a1 + c1 || c1 == a1 + b1)
        printf("right\n");
        else
        printf("wrong\n");
    }
}
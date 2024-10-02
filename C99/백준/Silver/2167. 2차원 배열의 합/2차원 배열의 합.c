#include <stdio.h>

int main() {
    int x, y, n, m, i1, j1;
    scanf("%d %d", &n, &m);
    int arr[301][301];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &arr[i][j]); 
        }
    }
    int s;
    scanf("%d", &s);
    for(int i = 0; i < s; i++) {
        scanf("%d %d %d %d", &x, &y, &i1, &j1); 
        int result = 0; 
        for(int i = x; i <= i1; i++) {
            for(int j = y; j <= j1; j++) {
                result += arr[i-1][j-1]; 
            }
        }
        printf("%d\n", result); 
    }
    return 0;
}
